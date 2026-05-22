import requests
import json
import os
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

# API key
WOS_API_KEY = os.getenv("WOS_API_KEY")
WOS_URL = "https://wos-api.clarivate.com/api/woslite/"

class WOSLite:
    def __init__(self):
        self.api_key = WOS_API_KEY
        self.session = requests.Session()

    # dois are unique well, sometimes it can be 2 because of the same article in different journals
    def search_doi(self, query):
        headers = {
            "X-ApiKey": self.api_key,
            "Content-Type": "application/json"
        }

        data = {
            "databaseId": "WOS",
            "usrQuery": f"DO=({query})",
            "count": 100,
            "firstRecord": 1,
        }

        response = self.session.get(WOS_URL, headers=headers, params=data)
        return response.json()
    
    def append_doi(self, data : pd.DataFrame):
        # create a WOS column if it does not exist
        if "WOS" not in data.columns:
            data["WOS"] = ""
            
        dois = data["DOI"].tolist()
        wos = []
        
        for doi in dois:
            result = self.search_doi(doi)
            if result["QueryResult"]["RecordsFound"] > 0:
                wos.append("Yes")
            else:
                wos.append("No")    
                
        data["WOS"] = wos
        
        return data