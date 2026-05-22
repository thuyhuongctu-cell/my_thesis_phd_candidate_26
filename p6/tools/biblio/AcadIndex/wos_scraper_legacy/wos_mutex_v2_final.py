import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedTagNameException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import pandas as pd
import threading
from portable_firefox_downloader import FirefoxPortableDownloader, FIREFOX64_VERSION_PATH

scopus_session = requests.Session()
wos_session = requests.Session()

WOS_URL = "https://mjl.clarivate.com/search-results"
ISSN_LIST_SPLIT_COUNT = 25
POSSIBLE_COLS = ["issn", "paper_title", "id"]
UNAVAILABLE_KEY = "Not available"
DATA_PATH = os.path.join(os.path.dirname(__file__), "output", "data")

ff_installer = FirefoxPortableDownloader()

# basically it verifies if some paper issn is in scopus or wos journals
# the driver should be run ONLY ONCE!!!!
class WOSVerifierMutex:
    def __init__(self):
        if not ff_installer.is_firefox_portable_installed():
            print("[WOSMutex] Firefox Portable is not installed. Installing...")
            ff_installer.setup()
        else:
            print("[WOSMutex] Firefox Portable already installed so proceeding.")

    def verify_with_df(self, data: pd.DataFrame):
        temp_dict = {}

        # Add id column
        data["ID"] = range(1, len(data) + 1)

        for column in data.columns:
            col_name = column.lower()
            if col_name in POSSIBLE_COLS:
                temp_dict[column] = data[column].tolist()

        issn_list = temp_dict["ISSN"]
        id_list = temp_dict["ID"]

        # Split the ISSN list into chunks of 25
        issn_chunks = [issn_list[i:i + ISSN_LIST_SPLIT_COUNT] for i in range(0, len(issn_list), ISSN_LIST_SPLIT_COUNT)]
        id_chunks = [id_list[i:i + ISSN_LIST_SPLIT_COUNT] for i in range(0, len(id_list), ISSN_LIST_SPLIT_COUNT)]

        threads = []

        self.results_lock = threading.Lock()
        self.results = {
            "ISSN": [],
            "ID": [],
            "WOS": []
        }

        # check if the data folder exists
        if not os.path.exists(DATA_PATH):
            os.makedirs(DATA_PATH)

        # Create a text file that contains the sizes of the ISSN chunks
        with open(os.path.join(DATA_PATH, "issn_chunks.txt"), "w") as f:
            for chunk in issn_chunks:
                f.write("Size of chunk: " + str(len(chunk)) + "\n")

        for i, chunk in enumerate(issn_chunks):
            thread = threading.Thread(target=self.__verify_chunk_with_handles, args=(chunk, id_chunks[i]))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        # Export the results to an xlsx file
        df = pd.DataFrame(self.results)
        df.to_excel(os.path.join(DATA_PATH, "results_v2.xlsx"), index=False)
        
        # change df issn column name to ISSN_V2
        df.rename(columns={"ISSN": "ISSN_V2"}, inplace=True)
        
        # Merge the results with the original data
        merged_df = pd.merge(data, df, on="ID", how="left")
        # drop id column
        merged_df.drop("ID", axis=1, inplace=True)
        
        merged_df.to_excel(os.path.join(DATA_PATH, "merged_results_v2.xlsx"), index=False)
        
        return merged_df
        
        
    def __verify_chunk_with_handles(self, issn_chunk: list, id_chunk: list):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.binary_location = FIREFOX64_VERSION_PATH
        firefox_options.add_argument("--headless")

        temp_browser = webdriver.Firefox(options=firefox_options)
        
        windows_data = {}

        for i in range(len(issn_chunk)):
            issn = issn_chunk[i]
            id = id_chunk[i]

            if issn == UNAVAILABLE_KEY or issn == "N/A" or issn != issn:
                with self.results_lock:
                    self.results["ID"].append(id)
                    self.results["ISSN"].append(issn)
                    self.results["WOS"].append(UNAVAILABLE_KEY)
                continue

            # Open a new tab
            temp_browser.execute_script("window.open('');")
            temp_browser.switch_to.window(temp_browser.window_handles[-1])
            temp_browser.get(WOS_URL)
            
            # associate that window with the id and issn consistently
            windows_data[temp_browser.window_handles[-1]] = {
                "id": id,
                "issn": issn
            }
            
        for window in windows_data:
            try:
                temp_browser.switch_to.window(window)
                search_box_win = WebDriverWait(temp_browser, 10).until(
                    EC.presence_of_element_located((By.ID, "search-box"))
                )
                
                print("Searching for ISSN and ID:", windows_data[window]["issn"], windows_data[window]["id"])
                
                sleep(2)
                
                search_box_win.clear()
                search_box_win.send_keys(windows_data[window]["issn"])
                
                search_button_win = WebDriverWait(temp_browser, 10).until(
                    EC.element_to_be_clickable((By.ID, "search-button"))
                )
                
                temp_browser.execute_script("arguments[0].click();", search_button_win)
                
                sleep(3)
                
                cards = WebDriverWait(temp_browser, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "app-journal-search-results"))
                ).find_elements(By.TAG_NAME, "mat-card")

                is_valid = self.__is_issn_valid(cards, windows_data[window]["issn"])
                
                with self.results_lock:
                    self.results["ID"].append(windows_data[window]["id"])
                    self.results["ISSN"].append(windows_data[window]["issn"])
                    self.results["WOS"].append("Yes" if is_valid else "No")
                
                # close the current tab
                temp_browser.close()
            except NoSuchElementException:
                print("Element not found. Skipping ISSN:", issn)
                with self.results_lock:
                    self.results["ID"].append(windows_data[window]["id"])
                    self.results["ISSN"].append(windows_data[window]["issn"])
                    self.results["WOS"].append(UNAVAILABLE_KEY)
                    
            temp_browser.switch_to.window(temp_browser.window_handles[0])

        temp_browser.quit()

    def __is_issn_valid(self, cards: list, issn: str):
        for card in cards:
            try:
                card_values = card.find_elements(By.CLASS_NAME, "search-results-value")
                issn_text = card_values[1].text.strip()
                print("New ISSN: ", issn_text, "Old ISSN: ", issn)
                all_issns = [i.strip() for i in issn_text.split("/")]

                if issn in all_issns:
                    return True
            except IndexError:
                print("No ISSN found in card!")
        return False
        