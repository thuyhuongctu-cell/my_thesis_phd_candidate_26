import requests
import json

MAX_ROWS = 100

class CrossrefWrapper:
    def __init__(self):
        self.base_url = "https://api.crossref.org/works/"
        self.session = requests.Session()
        self.request_count = 0
        
    def search_by_title(self, title : str):
        url = f"{self.base_url}?query.bibliographic={title}&rows={MAX_ROWS}"
        response = self.session.get(url)
        
        self.request_count += 1
        
        print(f"Request count: {self.request_count}")
        
        if response.status_code == 200:
            return response.json()
        
        print(response.text, response.status_code)
        
        return None
    
    def search_by_doi(self, doi : str):
        url = f"{self.base_url}{doi}"
        response = self.session.get(url)
        
        if response.status_code == 200:
            return response.json()
        
        return None