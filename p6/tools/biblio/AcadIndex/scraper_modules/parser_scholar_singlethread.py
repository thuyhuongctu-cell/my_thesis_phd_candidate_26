from bs4 import BeautifulSoup
# from wos_mutex_v2_final import WOSVerifierMutex, UNAVAILABLE_KEY
from .wos_multiprocess import WOSMultiProcessDOI, UNAVAILABLE_KEY
from .wos_api import WOSLite
from .scopus_verifier import ScopusAPIFetcher
import os
import pandas as pd
import re
# from habanero import Crossref
from .crossref_wrapper import CrossrefWrapper
import threading
import datetime
from time import sleep
from .paper_fetcher import MultiPaperFetcher
from .paper_filter import PaperFilter

from .scraper_config import ScraperConfig

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(BASE_PATH, "..", "html")
JSON_PATH = os.path.join(BASE_PATH, "..", "json")
OUTPUT_PATH = os.path.join(BASE_PATH, "..", "output")
DATA_PATH = os.path.join(OUTPUT_PATH, "..", "data")
BAD_PATH = os.path.join(BASE_PATH, "..", "bad")

FILES_PER_THREAD = 25
FETCHER_THREADS = 4

cr_wrapper = CrossrefWrapper()
         
# TODO: Remove ST and make support aiohttp
class ParserScholarLite:
    def __init__(self, use_wos_api : bool = True, use_indexers : bool = True) -> None:
        self.use_wos_api = use_wos_api
        self.titles = set()
        self.title_lock = threading.Lock()
        self.__output_path = ""
        self.use_indexers = use_indexers
        
        self.mapped_titles = {
            # Lets asume that the title is the key and the following are the values
            # Link, Author, Cite.
            # This is for the case that the elements maybe not found in crossref
        }
        
        self.load_config()
        
    def load_config(self):
        self.config = ScraperConfig()
        
    def __prepare_fallback(self, doc : BeautifulSoup):
        paper_tag = doc.select("[data-lid]")
        
        try:
            for result in paper_tag:
                title = result.select('h3')[0].get_text()
                title = re.sub(r'\[.*?\]', '', title)
                title = title.strip()
                title = " ".join(title.split())
                
                link = result.select('a')[0]['href']
                author = result.select('div')[0].get_text()
                
                with self.title_lock:
                    self.mapped_titles[title] = {
                        'Link': link,
                        'Author': author
                    }
        except Exception as e:
            print('Error with title: ', title, "Reason: ", e)
        
    def get_tags(self, doc : BeautifulSoup):
        paper_tag = doc.select("[data-lid]")
        cite_tag = doc.select("[title=Cite] + a")
        link_tag = doc.find_all("h3", {"class":"gs_rt"})
        author_tag = doc.find_all("div", {"class":"gs_a"})

        return paper_tag, cite_tag, link_tag, author_tag
     
    def __save_title(self, paper_tag):
        for tag in paper_tag:
            text = tag.select('h3')[0].get_text()
            
            # remove "[PDF]", "[HTML]" and "[LIBRO]" from text
            text = re.sub(r'\[.*?\]', '', text)
            text = text.strip()
            text = " ".join(text.split())
            
            with self.title_lock:
                self.titles.add(text)

    def get_link(self, link_tag):
        links = []

        for i in range(len(link_tag)):
            links.append(link_tag[i].select('a')[0]['href'])

        return links
        
    def process_html_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            # read the content of the file and parse it with BeautifulSoup
            soup = BeautifulSoup(f.read(), "lxml")
            
            # function for the get content of each page
            doc = soup
            # function for the collecting tags
            paper_tag,cite_tag,link_tag,author_tag = self.get_tags(doc)
            
            self.__prepare_fallback(doc)

            # get this element gs_hdr_tsi
            search_id = doc.find("input", {"name":"q"})
            self.__output_path = re.sub(r'[<>:"/\\|?*]', '_', search_id['value'])
            
            # self.fetch_paper_data(paper_tag)
            self.__save_title(paper_tag)
            
    def verify_wos(self, issn_list):
        # split the list into 10 parts
        threads = []
        issn_lists = [issn_list[i:i + 10] for i in range(0, len(issn_list), 10)]

        for issn_list in issn_lists:
            thread = threading.Thread(target=self.__verify_wos_thread, args=(issn_list,))
            thread.start()
            threads.append(thread)
            
        # Wait for all threads to complete
        thread : threading.Thread
        for thread in threads:
            thread.join()
            
    def __read_htmls_path(self, path : str):
        if not os.path.exists(path):
            raise FileNotFoundError(f"[ERROR] Path {path} doesn't exist.")
            
        # read all html files including the subdirectories
        threads = []

        thread_count = 0
        file_count = 0
        
        # load the config
        files_per_t = self.config.files_per_thread
        
        for root, _, files in os.walk(path):
            for file in files:
                if not file.endswith(".html"): continue
                # create a thread for each 10 html files
                file_path = os.path.join(root, file)
                thread = threading.Thread(target=self.process_html_file, args=(file_path,))
                thread.start()
                threads.append(thread)
                
                file_count += 1
                if file_count % files_per_t == 0:
                    # Wait for all threads in the current batch to finish
                    t: threading.Thread
                    for t in threads[thread_count:]:
                        t.join()
                    # Reset thread list for the next batch
                    threads = []
                    thread_count += 1
                    
        # Wait for all threads to complete
        thread : threading.Thread
        for thread in threads:
            thread.join()
            
    def __setup_output_path(self, path : str):
        today = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        # get the last part of the path
        # lets assume that is the query name
        query_name = self.__output_path
        target_path = os.path.join(OUTPUT_PATH, f"{query_name}_output")
        
        # we need this because we can save scrape data between times
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        
        # create a folder with the today thing
        target_path = os.path.join(target_path, today)
        
        # so we don't need the file name with time in the output
        if not os.path.exists(target_path):
            os.makedirs(target_path)
            
        return target_path
    
    def __check_indexers(self, df : pd.DataFrame):
        if self.use_wos_api:
            wos_verify = WOSLite()
            df = wos_verify.append_doi(df)
        else:
            wos_verify = WOSMultiProcessDOI()
            df = wos_verify.verify_doi(df)
        
        scopus_verifier = ScopusAPIFetcher()
        df = scopus_verifier.fetch_scopus_by_doi(df)
        
        # drop ID and ISSN_V2 columns if they exist
        if 'id' in df.columns:
            df.drop('id', axis=1, inplace=True)
            
        if 'ISSN_V2' in df.columns:
            df.drop('ISSN_V2', axis=1, inplace=True)
            
        return df
    
    def __save_unfetched(self, unfetched_titles : dict, target_path : str):
        # create a new dictionary with the unfetched titles and the mapped data
        new_dict = {}
        for title in unfetched_titles:
            new_dict[title] = self.mapped_titles.get(title, {})
            
        # THERE ARE 3 COLS, THE TITLE, THE LINK AND THE AUTHOR
        unfetched_df = pd.DataFrame(new_dict).T.reset_index()
        unfetched_df.columns = ['Title', 'Link', 'Author']
        
        
        unfetched_df.to_excel(os.path.join(target_path, "unfetched_titles.xlsx"), index=False)
            
    def read_htmls(self, to_excel = False, path : str = HTML_PATH):
        # setup the filter
        p_filter = PaperFilter(
            config=self.config.filter_data,
            use_indexing=self.use_indexers
        )
        
        # reset if we are going to read again
        self.titles = set()
        
        self.__read_htmls_path(path)
        
        target_path = self.__setup_output_path(path)
        
        titles_list = list(self.titles)

        # separation of concerns
        mpf = MultiPaperFetcher(
            thread_count=self.config.fetch_thread_count,
            similarity_threshold=self.config.title_similar_threshold
        )
        cached = mpf.fetch_papers_data(titles_list)
        
        self.__save_unfetched(mpf.unfetched_titles, target_path)
    
        # save the cached data to a csv file
        df = pd.DataFrame(cached)
        
        # remove rows with null dois
        df = df[df['DOI'] != 'NULL']
        
        # count duplicated DOIs
        dupes_doi = df.duplicated(subset=["DOI"]).sum()
        
        # remove rows with duplicated DOIs
        df.drop_duplicates(subset=['DOI'], inplace=True)
        
        # create excel, why you may ask?
        # because we need to backup before something very weird happens
        
        if self.use_indexers:
            # security check
            df.to_excel(os.path.join(target_path, f"papers_no_indexers.xlsx"), index=False)
            df = self.__check_indexers(df)
            df['WOS and Scopus'] = df.apply(lambda row: "Yes" if row['WOS'] == "Yes" and row['Scopus'] == "Yes" else "No", axis=1)
        
        # here we filter the data
        p_filter.setup(df)
        df = p_filter.filter_papers()
        
        less_cit = p_filter.df_stats["niche_papers"]
        below_year = p_filter.df_stats["below_year"]
            # Then, create a new column called "WOS and Scopus" based on the filtered data


        # Clear the screen
        # os.system('cls' if os.name == 'nt' else 'clear')
        # Get the username from computer
        user_name = os.getlogin()
        
        # this should always be true
        if (user_name != ''):
            user_name = user_name.replace('.', ' ').title()
            df['Scraper Responsible'] = user_name

        # ask for user name to create a new column
        # user_name = input("Introduce tu nombre y apellido: ")
        
        # create a new column with the user name and fill all the rows with the user name
        filename = f'scraped_papers'

        if not to_excel:
            df.to_csv(os.path.join(target_path, f'{filename}.csv'), index=False)
        else:
            df.to_excel(os.path.join(target_path, f'{filename}.xlsx'), index=False)
            
        adjustable_name = 'with_indexers' if self.use_indexers else 'normal'
            
        # create a log file
        log_file = os.path.join(target_path, f'scraped_data_{adjustable_name}.log')
        
        with open(log_file, "w") as f:
            # describe the count of df
            f.write(f"Total papers scraped: {len(df)}\n")
            f.write(f"Total papers with DOI: {len(df[df['DOI'] != 'NULL'])}\n")
            f.write(f"Total papers without DOI: {len(df[df['DOI'] == 'NULL'])}\n")
            f.write(f"Total papers with ISSN: {len(df[df['ISSN'] != UNAVAILABLE_KEY])}\n")
            f.write(f"Total papers without ISSN: {len(df[df['ISSN'] == UNAVAILABLE_KEY])}\n")


            f.write(f"Total papers with duplicated DOIs: {dupes_doi}\n")
            f.write(f"Total papers with less than 10 references or citations: {less_cit}\n")
            f.write(f"Total papers below {p_filter.year}: {below_year}\n")
            
            if self.use_indexers:
                not_indexed = p_filter.df_stats["not_indexed"]
                f.write(f"Total papers without indexers: {not_indexed}\n")
                f.write(f"Total papers with WOS: {len(df[df['WOS'] == 'Yes'])}\n")
                f.write(f"Total papers with WOS and Scopus: {len(df[df['WOS and Scopus'] == 'Yes'])}\n")
            
            # write the scraper responsible
            f.write(f"Scraper responsible: {user_name}\n")
            
        # save the titles to a file
        with open(os.path.join(target_path, f"titles.txt"), "w", encoding="utf-8") as f:
            for title in self.titles:
                f.write(f"{title}\n")
                
        # save to an excel the OG Title | Mismatched Title
        mismatch_df = pd.DataFrame(mpf.mismatched_titles.items(), columns=['Original Title', 'Mismatched Title'])