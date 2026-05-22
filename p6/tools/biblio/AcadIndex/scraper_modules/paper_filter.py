import pandas as pd
import os
import json

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.abspath(os.path.join(FILE_PATH, "..", "config", "filter.json"))

class PaperFilter:
    def __init__(self, config : dict = None, use_indexing : bool = False) -> None:
        # self.df = df
        
        # save the stats for debugging
        self.df_stats = {
            "not_indexed": 0,
            "niche_papers": 0,
            "below_year": 0,
        }
        
        self.year = 0
        self.ref_count = 0
        self.cit_count = 0
        
        if config is not None:
            self.__load_config(config)
        else:
            self.__parse_filter()
            
        self.use_indexing = use_indexing
        
    def __load_config(self, data : dict):
        self.year  = data["min_year"]
        self.ref_count = data["ref_count"]
        self.cit_count = data["cit_count"]
    
    def __parse_filter(self):
        # read the filter.json file
        with open(JSON_FILE, "r") as f:
            data = json.load(f)
            
        self.year = data["min_year"]
        self.ref_count = data["ref_count"]
        self.cit_count = data["cit_count"]
        
    def setup(self, df : pd.DataFrame):
        self.df = df
        self.filter_papers()
        
    def set_year_to_filter(self, year : int):
        self.year = year
        
    def set_ref_cit_count(self, ref_count : int, cit_count : int):
        self.ref_count = ref_count
        self.cit_count = cit_count
        
    def __save_bad_stats(self):
        self.df_stats["below_year"] = (self.df["Year"] < self.year).sum()
        self.df_stats["niche_papers"] = ((self.df['Times Referenced'] < self.cit_count) & (self.df['Reference Count'] < self.ref_count)).sum()
        
        if self.use_indexing:
            self.df_stats["not_indexed"] = ((self.df["WOS"].isin(["No", "Not available"])) & (self.df["Scopus"].isin(["No", "Not available"]))).sum()
        
    def filter_papers(self):
        self.__save_bad_stats()
        self.remove_papers_by_year()
        self.ref_cit_count_excluder()
        
        if self.use_indexing:
            self.remove_papers_without_indexer()
        
        return self.get_filtered_df()
        
    def remove_papers_by_year(self):
        # remove papers that are older than the year
        self.df = self.df[self.df["Year"] >= self.year]
        
    def ref_cit_count_excluder(self):
        # remove papers that have less than ref_count references and cit_count citations
        # if they are not on the year 2023 or newer
        self.df = self.df[(
            (self.df['Times Referenced'] >= self.cit_count) & (self.df['Reference Count'] >= self.ref_count) |
            (self.df['Year'].isin([2022, 2023]))
        )]
        
    def remove_papers_without_indexer(self):
        # remove papers that are not indexed in scopus or wos
        self.df = self.df[(self.df["WOS"] == "Yes") | (self.df["Scopus"] == "Yes")]
        
    def get_filtered_df(self) -> pd.DataFrame:
        return self.df