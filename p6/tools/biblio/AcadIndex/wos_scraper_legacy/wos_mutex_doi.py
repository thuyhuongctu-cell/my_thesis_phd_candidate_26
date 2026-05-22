import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import UnexpectedTagNameException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import pandas as pd
import threading
from portable_firefox_downloader import FirefoxPortableDownloader, FIREFOX64_VERSION_PATH, FIREFOX_PROFILE_PATH

WOS_URL = "https://www.webofscience.com/wos/woscc/basic-search"
DOI_LIST_SPLIT_COUNT = 50
POSSIBLE_COLS = ["issn", "paper_title", "id", "doi"]
UNAVAILABLE_KEY = "Not available"
DATA_PATH = os.path.join(os.path.dirname(__file__), "output", "data")
DOI_KEY = "DOI"

ff_installer = FirefoxPortableDownloader()

# basically it verifies if some paper issn is in scopus or wos journals
# the driver should be run ONLY ONCE!!!!
class WOSVerifierMutexDOI:
    def __init__(self):
        if not ff_installer.is_firefox_portable_installed():
            print("[WOSMutex] Firefox Portable is not installed. Installing...")
            ff_installer.setup()
        else:
            print("[WOSMutex] Firefox Portable already installed so proceeding.")
            
    def __firefox_cleanups(self):
        # call the batch file that deletes rust_mozprofile folders from temp
        os.system("delete_trash.bat")

    def verify_doi(self, data: pd.DataFrame):
        temp_dict = {}

        # Add id column
        data["ID"] = range(1, len(data) + 1)

        for column in data.columns:
            col_name = column.lower()
            if col_name in POSSIBLE_COLS:
                temp_dict[column] = data[column].tolist()

        doi_list = temp_dict[DOI_KEY]
        id_list = temp_dict["ID"]

        # Split the ISSN list into chunks of 25
        doi_chunks = [doi_list[i:i + DOI_LIST_SPLIT_COUNT] for i in range(0, len(doi_list), DOI_LIST_SPLIT_COUNT)]
        id_chunks = [id_list[i:i + DOI_LIST_SPLIT_COUNT] for i in range(0, len(id_list), DOI_LIST_SPLIT_COUNT)]

        threads = []

        self.results_lock = threading.Lock()

        self.results = {
            DOI_KEY: [],
            "ID": [],
            "WOS": []
        }

        # check if the data folder exists
        if not os.path.exists(DATA_PATH):
            os.makedirs(DATA_PATH)

        # Create a text file that contains the sizes of the ISSN chunks
        with open(os.path.join(DATA_PATH, "doi_chunks.txt"), "w") as f:
            for chunk in doi_chunks:
                f.write("Size of chunk: " + str(len(chunk)) + "\n")

        for i, chunk in enumerate(doi_chunks):
            thread = threading.Thread(target=self.__verify_chunk_with_handles, args=(chunk, id_chunks[i]))
            thread.start()
            threads.append(thread)

        thread : threading.Thread
        for thread in threads:
            thread.join()

        # Export the results to an xlsx file
        df = pd.DataFrame(self.results)
        df.to_excel(os.path.join(DATA_PATH, "results_v2.xlsx"), index=False)
        
        # change df issn column name to ISSN_V2
        df.rename(columns={DOI_KEY: f"{DOI_KEY}_V2"}, inplace=True)
        
        # Merge the results with the original data
        merged_df = pd.merge(data, df, on="ID", how="left")
        # drop id column
        merged_df.drop("ID", axis=1, inplace=True)
        
        merged_df.to_excel(os.path.join(DATA_PATH, "merged_results_v2.xlsx"), index=False)
        
        self.__firefox_cleanups()
        
        return merged_df
        
    def __select_doi_option(self, doc_type_options: list):
        for option in doc_type_options:
            if option.text == DOI_KEY:
                option.click()
                break
        
    def __verify_chunk_with_handles(self, doi_chunk: list, id_chunk: list):
        firefox_options = webdriver.FirefoxOptions()
        firefox_profile = webdriver.FirefoxProfile(FIREFOX_PROFILE_PATH)
        
        firefox_options.profile = firefox_profile
        firefox_options.binary_location = FIREFOX64_VERSION_PATH
        firefox_options.set_preference("dom.popup_maximum", DOI_LIST_SPLIT_COUNT * 2)
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        firefox_options.add_argument("--disable-gpu")
        firefox_options.add_argument("--disable-extensions")
        firefox_options.add_argument("--disable-infobars")

        temp_browser = webdriver.Firefox(options=firefox_options)
        
        # manage timeouts
        temp_browser.set_page_load_timeout(10)
        
        windows_data = {}
        
        doi_key_mini = DOI_KEY.lower()
        
        for i in range(len(doi_chunk)):
            print(f"Current iteration: {i} DOI: {doi_chunk[i]} ID: {id_chunk[i]}")

        for i in range(len(doi_chunk)):
            doi = doi_chunk[i]
            id = id_chunk[i]

            # Open a new tab
            try:
                temp_browser.execute_script("window.open('');")
                temp_browser.switch_to.window(temp_browser.window_handles[-1])
                temp_browser.get(WOS_URL)
                
                WebDriverWait(temp_browser, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
                
                # associate that window with the id and issn consistently
                windows_data[id] = {
                    "window": temp_browser.window_handles[-1],
                    "doi": doi
                }
            except TimeoutException as e:
                print("[ERROR] Timed out, reason:", e)
                continue

        counter = 0

        for id in windows_data:
            doi, window = windows_data[id][doi_key_mini], windows_data[id]["window"]
            print("[INFO] Searching for DOI and ID:", doi, id)
            
            try:
                temp_browser.switch_to.window(window)
                
                document_selector = temp_browser.find_elements(By.TAG_NAME, "wos-select")
                
                # the third element is the one we want
                document_selector[2].click()
                
                sleep(1)
                
                # select the doi option 
                doc_type_options = document_selector[2].find_elements(By.TAG_NAME, "div")
                
                self.__select_doi_option(doc_type_options)
                    
                sleep(1)
                
                search_box = temp_browser.find_elements(By.ID, "mat-input-0")[0]
                search_box.clear()
                
                search_box.send_keys(doi)
                search_box.send_keys(Keys.RETURN)
                
                sleep(3)
                
                # find span with classname "brand-blue"
                result_count = temp_browser.find_elements(By.CLASS_NAME, "brand-blue")
                
                print("Result count: ", len(result_count), "DOI: ", doi)

                if result_count is None or len(result_count) == 0:
                    temp_browser.close()
                    raise NoSuchElementException("Element not found")
                
                result_count = result_count[0].text
                
                if result_count != "1":
                    raise UnexpectedTagNameException("More than one result found for a unique DOI. Skipping...")
                
                with self.results_lock:
                    self.results["ID"].append(id)
                    self.results[DOI_KEY].append(doi)
                    self.results["WOS"].append("Yes")
                
                # close the current tab
                temp_browser.close()
            except NoSuchElementException:
                print("[WARNING] Element not found. Skipping DOI:", doi)
                # no instead of unavailable because doi is unique
                with self.results_lock:
                    self.results["ID"].append(id)
                    self.results[DOI_KEY].append(doi)
                    self.results["WOS"].append("No")
            except UnexpectedTagNameException as e:
                print("[WTF__LOL] More than one result found for a unique DOI. Skipping...")
                    
            temp_browser.switch_to.window(temp_browser.window_handles[0])
            counter += 1

        temp_browser.quit()

        print(f"Process finished. {counter} DOIs processed of {len(doi_chunk)} and also window count {len(windows_data)}.")
        print("Thread finished.")
        
df = pd.read_excel("output/papers_not_scopus_wos_2024-05-29-20-25-22.xlsx")
verifier = WOSVerifierMutexDOI()
merged_df = verifier.verify_doi(df)