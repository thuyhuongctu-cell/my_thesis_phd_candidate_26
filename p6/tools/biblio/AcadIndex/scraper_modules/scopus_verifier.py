import requests
from dotenv import load_dotenv
import os
import pandas as pd
import threading
import time

load_dotenv()

SCOPUS_API_KEY = os.getenv("SCOPUS_API_KEY")
SCOPUS_SEARCH_URL = "https://api.elsevier.com/content/search/scopus"
SUCCESS_CODE = 200
MAX_REQUESTS_PER_SEC = 6
FILE_PATH = os.path.join(os.path.dirname(__file__), "output", "data")
NOT_AVAILABLE = "Not available"

class ScopusAPIFetcher:
    def __init__(self):
        self.scopus_sess = requests.Session()
        # self.base_url = "https://api.elsevier.com/content/serial/title"
        
    def fetch_scopus_by_doi(self, df : pd.DataFrame):
        # create a column called "Scopus" in the dataframe
        df["Scopus"] = ""
        counter = 0
        
        for index, row in df.iterrows():
            doi = row["DOI"]
            
            # skip irrelevant ones
            if doi == NOT_AVAILABLE or pd.isnull(doi) or doi == "N/A":
                df.loc[index, "Scopus"] = NOT_AVAILABLE
                continue
            
            if counter == MAX_REQUESTS_PER_SEC:
                print("Sleeping for 1 second to avoid rate limiting...")
                time.sleep(1)
                counter = 0
    
            scopus_result = self.scopus_sess.get(SCOPUS_SEARCH_URL, params={
                "apiKey": SCOPUS_API_KEY,
                "query": f"DOI({doi})"
            })
            
            counter += 1
            
            if scopus_result.status_code != SUCCESS_CODE:
                print(f"Error fetching data for DOI {doi}")
                continue
            
            scopus_result_json = scopus_result.json()

            if "search-results" in scopus_result_json:
                search_results = scopus_result_json["search-results"]
                total_results = search_results["opensearch:totalResults"]
                
                if total_results != "0":
                    df.loc[index, "Scopus"] = "Yes"
                else:
                    df.loc[index, "Scopus"] = "No"
                
                print(f"Scopus results for DOI {doi}: {total_results}")
        # create data dir if it doesn't exist
        if not os.path.exists(FILE_PATH):
            os.makedirs(FILE_PATH)
        
        # create an excel file with the results
        df.to_excel(os.path.join(FILE_PATH,"scopus_results_doi.xlsx"), index=False)
        
        return df
        
    def fetch_scopus_by_issn(self, df : pd.DataFrame):
        # create a column called "Scopus" in the dataframe
        df["Scopus"] = ""
        counter = 0
        
        for index, row in df.iterrows():
            issn = row["ISSN"]
            
            # skip irrelevant ones
            if issn == NOT_AVAILABLE or pd.isnull(issn) or issn == "N/A":
                df.loc[index, "Scopus"] = NOT_AVAILABLE
                continue
            
            if counter == MAX_REQUESTS_PER_SEC:
                print("Sleeping for 1 second to avoid rate limiting...")
                time.sleep(1)
                counter = 0
    
            scopus_result = self.scopus_sess.get(SCOPUS_SEARCH_URL, params={
                "apiKey": SCOPUS_API_KEY,
                "query": f"ISSN({issn})"
            })
            
            counter += 1
            
            if scopus_result.status_code != SUCCESS_CODE:
                print(f"Error fetching data for ISSN {issn}")
                continue
            
            scopus_result_json = scopus_result.json()

            if "search-results" in scopus_result_json:
                search_results = scopus_result_json["search-results"]
                total_results = search_results["opensearch:totalResults"]
                
                if total_results != "0":
                    df.loc[index, "Scopus"] = "Yes"
                else:
                    df.loc[index, "Scopus"] = "No"
                
                print(f"Scopus results for ISSN {issn}: {total_results}")
        # create data dir if it doesn't exist
        if not os.path.exists(FILE_PATH):
            os.makedirs(FILE_PATH)
        
        # create an excel file with the results
        df.to_excel(os.path.join(FILE_PATH,"scopus_results.xlsx"), index=False)
        
        return df