import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedTagNameException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
import threading
from portable_firefox_downloader import FirefoxPortableDownloader, FIREFOX64_VERSION_PATH

scopus_session = requests.Session()
wos_session = requests.Session()

WOS_URL = "https://mjl.clarivate.com/home"
ISSN_LIST_SPLIT_COUNT = 25
POSSIBLE_COLS = ["issn", "paper_title", "id"]

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
        data["id"] = range(1, len(data) + 1)

        for column in data.columns:
            col_name = column.lower()
            if col_name in POSSIBLE_COLS:
                temp_dict[column] = data[column].tolist()

        issn_list = temp_dict["ISSN"]
        id_list = temp_dict["id"]

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

        # Create a text file that contains the sizes of the ISSN chunks
        with open("issn_sizes.txt", "w") as f:
            for chunk in issn_chunks:
                f.write("Size of chunk: " + str(len(chunk)) + "\n")

        for i, chunk in enumerate(issn_chunks):
            thread = threading.Thread(target=self.__verify_chunk, args=(chunk, id_chunks[i]))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        # Export the results to an xlsx file
        df = pd.DataFrame(self.results)
        df.to_excel("results.xlsx", index=False)

    def __verify_chunk(self, issn_chunk: list, id_chunk: list):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.binary_location = FIREFOX64_VERSION_PATH
        firefox_options.add_argument("--headless")

        temp_browser = webdriver.Firefox(options=firefox_options)

        for i in range(len(issn_chunk)):
            issn = issn_chunk[i]
            id = id_chunk[i]

            if issn == "N/A" or issn != issn:
                with self.results_lock:
                    self.results["ID"].append(id)
                    self.results["ISSN"].append(issn)
                    self.results["WOS"].append("N/A")
                continue

            try:
                # Open a new tab
                temp_browser.execute_script("window.open('');")
                temp_browser.switch_to.window(temp_browser.window_handles[-1])
                temp_browser.get(WOS_URL)

                # Wait for the search box and enter ISSN
                search_box = WebDriverWait(temp_browser, 10).until(
                    EC.presence_of_element_located((By.ID, "search-box"))
                )

                sleep(4)

                search_box.clear()
                search_box.send_keys(issn)

                # Wait for the search button and click it
                search_button = WebDriverWait(temp_browser, 10).until(
                    EC.element_to_be_clickable((By.ID, "search-button"))
                )

                sleep(4)

                temp_browser.execute_script("arguments[0].click();", search_button)

                sleep(4)

                # Wait for search results to load and get cards
                cards = WebDriverWait(temp_browser, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "app-journal-search-results"))
                ).find_elements(By.TAG_NAME, "mat-card")

                is_valid = self.__is_issn_valid(cards, issn)

                with self.results_lock:
                    self.results["ID"].append(id)
                    self.results["ISSN"].append(issn)
                    self.results["WOS"].append("Yes" if is_valid else "No")

            except NoSuchElementException:
                print("Element not found. Skipping ISSN:", issn)
                with self.results_lock:
                    self.results["ID"].append(id)
                    self.results["ISSN"].append(issn)
                    self.results["WOS"].append("N/A")

            # Close the current tab and switch back to the main window
            temp_browser.close()
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
# read the data from xlsx file
last_scrape = pd.read_excel("output/scrape_2024-05-26.xlsx")

# last_scrape = last_scrape.head(10)

# print all elements from issn column
print(last_scrape["ISSN"])

# print columns data types
print(last_scrape.dtypes)

wos_verifier = WOSVerifierMutex()
wos_verifier.verify_with_df(last_scrape)
        