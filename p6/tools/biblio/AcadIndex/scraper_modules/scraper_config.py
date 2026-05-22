import os
import json

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.abspath(os.path.join(FILE_PATH, "..", "config", "config.json"))

class ScraperConfig:
    def __init__(self) -> None:
        self.title_similar_threshold = 0.0
        self.fetch_thread_count = 0
        self.files_per_thread = 0
        
        self.filter_data = {
            "min_year": 0,
            "ref_count": 0,
            "cit_count": 0,
        }
        
        self.__parse_config()

    def __load_config(self, data : dict):
        target_data : dict = data["scraper"]
        
        self.title_similar_threshold = target_data["title_similar_threshold"]
        self.fetch_thread_count = target_data["fetch_thread_count"]
        self.files_per_thread = target_data["files_per_thread"]
        
    def __load_filter_config(self, data : dict):
        target_data : dict = data["filter"]
        
        self.filter_data["min_year"] = target_data["min_year"]
        self.filter_data["ref_count"] = target_data["ref_count"]
        self.filter_data["cit_count"] = target_data["cit_count"]
        
    def __parse_config(self):
        # read the filter.json file
        with open(JSON_FILE, "r") as f:
            data = json.load(f)
            
        print(data)
            
        # there are two relevant sections the filter and the config
        self.__load_config(data)
        self.__load_filter_config(data)
