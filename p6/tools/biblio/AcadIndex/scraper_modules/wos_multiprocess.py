import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedTagNameException
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import Manager
from time import sleep
from .firefox_handlers.portable_firefox_downloader import FirefoxPortableDownloader, FIREFOX64_VERSION_PATH, FIREFOX_PROFILE_PATH
from .firefox_handlers.simple_firefox import SimpleFirefox

WOS_URL = "https://www.webofscience.com/wos/woscc/basic-search"
DOI_LIST_SPLIT_COUNT = 50
POSSIBLE_COLS = ["issn", "paper_title", "id", "doi"]
UNAVAILABLE_KEY = "Not available"
DATA_PATH = os.path.join(os.path.dirname(__file__), "output", "data")
DOI_KEY = "DOI"
MAX_PROCESSES = 10

class WOSMultiProcessDOI:
    def __init__(self):
        if not os.path.exists(DATA_PATH):
            os.makedirs(DATA_PATH)
            
        self.processed_dois_count = 0
        
        ff_installer = FirefoxPortableDownloader()
        if not ff_installer.is_firefox_portable_installed():
            ff_installer.setup()

    def __process_doi_chunk(self, doi_chunk : list, id_chunk: list, return_dict : dict, process_id : int):
        firefox = SimpleFirefox(FIREFOX_PROFILE_PATH, FIREFOX64_VERSION_PATH)
        temp_browser = firefox.instance()
        temp_browser.set_page_load_timeout(10)
        
        results = {
            "ID": [],
            DOI_KEY: [],
            "WOS": []
        }
        
        for doi, id in zip(doi_chunk, id_chunk):
            print(f"[Process {process_id}] Processing DOI: {doi}, ID: {id}")

            try:
                temp_browser.get(WOS_URL)
                WebDriverWait(temp_browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                
                # Select DOI option
                document_selector = WebDriverWait(temp_browser, 10).until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, "wos-select"))
                )
                
                document_selector[2].click()
                
                sleep(1)

                doc_type_options = document_selector[2].find_elements(By.TAG_NAME, "div")

                for option in doc_type_options:
                    if option.text == DOI_KEY:
                        option.click()
                        break
    
                sleep(1)
                
                # Enter DOI and search
                search_box = temp_browser.find_element(By.ID, "mat-input-0")
                search_box.clear()
                search_box.send_keys(doi)
                search_box.send_keys(Keys.RETURN)
                sleep(3)
                
                # Check result count
                result_count = temp_browser.find_elements(By.CLASS_NAME, "brand-blue")

                if not result_count:
                    raise NoSuchElementException("No results found.")
                
                res_data = result_count[0].text
                count = int(res_data)
                
                result_key = "Yes" if count == 1 else "Yes (Has different versions)"
                
                print(f"[Process {process_id}] Found {count} results for DOI: {doi}")
    
                results["ID"].append(id)
                results[DOI_KEY].append(doi)
                results["WOS"].append(result_key)
            except (NoSuchElementException, UnexpectedTagNameException):
                print(f"[Process {process_id}] No results found for DOI: {doi}")

                results["ID"].append(id)
                results[DOI_KEY].append(doi)
                results["WOS"].append("No")
            except TimeoutException:
                # this shouldn't happen but just in case
                results["ID"].append(id)
                results[DOI_KEY].append(doi)
                results["WOS"].append("Timeout")
        
        temp_browser.quit()
        return_dict[process_id] = results
        print(f"[Process {process_id}] Finished processing.")
            
    def __cleanup_firefox(self):
        os.system("delete_trash.bat")

    def verify_doi(self, data: pd.DataFrame):
        temp_dict = {}
        data["ID"] = range(1, len(data) + 1)

        for column in data.columns:
            col_name = column.lower()
            if col_name in POSSIBLE_COLS:
                temp_dict[column] = data[column].tolist()

        doi_list = temp_dict[DOI_KEY]
        id_list = temp_dict["ID"]
        doi_chunks = [doi_list[i:i + DOI_LIST_SPLIT_COUNT] for i in range(0, len(doi_list), DOI_LIST_SPLIT_COUNT)]
        id_chunks = [id_list[i:i + DOI_LIST_SPLIT_COUNT] for i in range(0, len(id_list), DOI_LIST_SPLIT_COUNT)]
        
        manager = Manager()
        return_dict = manager.dict()
        processes = []
        
        with ProcessPoolExecutor(max_workers=MAX_PROCESSES) as executor:
            for i, (doi_chunk, id_chunk) in enumerate(zip(doi_chunks, id_chunks)):
                process = executor.submit(self.__process_doi_chunk, doi_chunk, id_chunk, return_dict, i)
                processes.append(process)
            
            for process in as_completed(processes):
                process.result()
        
        # in this case we assume that the processes are done
        self.__cleanup_firefox()

        # Combine results from all processes
        final_results = {
            "ID": [],
            DOI_KEY: [],
            "WOS": []
        }

        for process_id in return_dict:
            for key in final_results:
                final_results[key].extend(return_dict[process_id][key])
        
        # Export the results to an xlsx file
        df = pd.DataFrame(final_results)
        df.to_excel(os.path.join(DATA_PATH, "results_v2.xlsx"), index=False)
        
        # Merge the results with the original data
        merged_df = pd.merge(data, df, on="ID", how="left")
        merged_df.drop("ID", axis=1, inplace=True)
        merged_df.to_excel(os.path.join(DATA_PATH, "merged_results_v2.xlsx"), index=False)
        
        return merged_df