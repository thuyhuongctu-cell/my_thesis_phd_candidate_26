from bs4 import BeautifulSoup
# from wos_mutex_v2_final import WOSVerifierMutex, UNAVAILABLE_KEY
from wos_multiprocess import WOSMultiProcessDOI, UNAVAILABLE_KEY
from wos_api import WOSLite
from scopus_verifier import ScopusAPIFetcher
import os
import pandas as pd
import re
# from habanero import Crossref
from lib.habanero_git.habanero import Crossref
import threading
import datetime
from time import sleep

cr = Crossref()

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(BASE_PATH, "html")
JSON_PATH = os.path.join(BASE_PATH, "json")
OUTPUT_PATH = os.path.join(BASE_PATH, "output")
DATA_PATH = os.path.join(OUTPUT_PATH, "data")
BAD_PATH = os.path.join(BASE_PATH, "bad")

FILES_PER_THREAD = 25
MAX_RETRIES = 3

cached = set()

class PaperFetcher:
    def __init__(self) -> None:
        pass
    
    def __get_proper_issn(self, item : dict) -> str:
        issn_list = item.get('ISSN')

        if not issn_list:
            return UNAVAILABLE_KEY
        
        # this means we can have e-ISSN or p-ISSN
        issn_types = item.get('issn-type')
        
        for issn_dict in issn_types:
            if issn_dict.get('type') == "electronic":
                return issn_dict.get('value')
            
        return issn_list[0]
        
    def fetch_data(self, papername: str, retries: int = MAX_RETRIES) -> dict | None:
        print("Obteniendo datos del paper ", papername)

        for attempt in range(retries):
            try:
                paper_data = self.retry_works(papername)
                message = paper_data.get('message')

                if not message:
                    return None

                items = message['items']

                # Check if any item matches the paper name
                for item in items:
                    item_title = item.get('title')

                    if not item_title:
                        continue

                    item_title = item_title[0]

                    if item_title.lower() == papername.lower():
                        return item

                # Fallback to the first item if no exact match found
                return items[0]

            except Exception as e:
                print(f"An error occurred while fetching data for {papername}: {e}")

                if attempt < retries - 1:
                    print(f"Retrying after {2 ** attempt} seconds...")
                    sleep(2 ** attempt)
                else:
                    print(f"All {retries} attempts failed. Unable to fetch data for {papername}.")
                    return None

    def retry_works(self, papername: str):
        for attempt in range(MAX_RETRIES):  # Retry 3 times
            try:
                paper_data = cr.works(query=papername)
                return paper_data
            except Exception as e:
                print(f"Failed to fetch data for {papername}. Retry attempt {attempt+1}. Error: {e}")
                sleep(2 ** attempt)  # Exponential backoff
        print(f"All attempts failed to fetch data for {papername}.")
        return None
        
    def extract_data(self, item : dict):
        title = item.get('title') # item['title'][0]
        
        if not title:
            print("Invalid title for item: ", item)
            return
        
        title = title[0]
        
        # save all authors separated by comma
        authors = []
        
        all_authors = item.get('author')
        
        # we don't care about invalid authors
        if not all_authors:
            return
        
        for author in all_authors:
            author_first = author.get('given')
            author_last = author.get('family')
            
            if not author_first or not author_last:
                continue
            
            # print(item['author'])
            author_name = author_first + " " + author_last
            authors.append(author_name)
            
        author = ", ".join(authors)

        # basically obtains the first year of the date-parts
        year = item.get('created').get('date-parts')[0]
        
        # obtain the year
        year = year[0]
        
        # reference ahh stuff.
        ref_count = item.get('reference-count')
        times_referenced = item.get('is-referenced-by-count')
        
        print(ref_count, times_referenced)
        
        doi = item['DOI']
        publisher = item['publisher']
        
        # get url
        url = item['resource']['primary']['URL']
        
        # get issn, also its possible that some papers may not have an issn
        issn = self.__get_proper_issn(item)
        
        # create a dict containing the data
        return {
            'Title' : title,
            'Author' : author,
            'Year' : year,
            'DOI' : doi,
            'Publisher' : publisher,
            'URL' : url,
            'Reference Count' : ref_count,
            'Times Referenced' : times_referenced,
            'ISSN' : issn
        }
        
    def is_on_wos(self, doi : str) -> bool:
        pass
         
class ParserScholar:
    def __init__(self, use_wos_api : bool = True) -> None:
        # setup the crossref object
        # make self.cached to have the same stuff returning from the previous snippet
        self.cached = {
            'Title' : [],
            'Author' : [],
            'Year' : [],
            'DOI' : [],
            'Publisher' : [],
            'URL' : [],
            'Reference Count' : [],
            'Times Referenced' : [],
            'ISSN' : [],
        }
        
        self.use_wos_api = use_wos_api
        
    def get_tags(self, doc : BeautifulSoup):
        paper_tag = doc.select("[data-lid]")
        cite_tag = doc.select("[title=Cite] + a")
        link_tag = doc.find_all("h3", {"class":"gs_rt"})
        author_tag = doc.find_all("div", {"class":"gs_a"})

        return paper_tag, cite_tag, link_tag, author_tag
    
    def get_papertitle(self, paper_tag):
        paper_names = []
        dois = []

        for tag in paper_tag:
            text = tag.select('h3')[0].get_text()
            
            # remove "[PDF]", "[HTML]" and "[LIBRO]" from text
            text = re.sub(r'\[.*?\]', '', text)
            text = text.strip()
            text = " ".join(text.split())
            
            print("TEXTS: ", text)

            try:
                result = cr.works(query = text)
                dois.append(result['message']['items'][0]['DOI'])
            except Exception as e:
                print(f"Error: {e}")
                dois.append("NULL")
            
            paper_names.append(text)

        return paper_names, dois
    
    def save_paper_data(self, data : dict):
        # add data to the cached dict
        self.cached['Title'].append(data['Title'])
        self.cached['Author'].append(data['Author'])
        self.cached['Year'].append(data['Year'])
        self.cached['DOI'].append(data['DOI'])
        self.cached['Publisher'].append(data['Publisher'])
        self.cached['URL'].append(data['URL'])
        self.cached['Reference Count'].append(data['Reference Count'])
        self.cached['Times Referenced'].append(data['Times Referenced'])
        self.cached['ISSN'].append(data['ISSN'])

    def fetch_paper_data(self, paper_tag):
        for tag in paper_tag:
            text = tag.select('h3')[0].get_text()
            
            # remove "[PDF]", "[HTML]" and "[LIBRO]" from text
            text = re.sub(r'\[.*?\]', '', text)
            text = text.strip()
            text = " ".join(text.split())

            fetcher = PaperFetcher()
            items = fetcher.fetch_data(text)
            
            if not items:
                continue
            
            print("Paper title: ", text)
            
            data = fetcher.extract_data(items)
            
            # why we would want to save invalid data?
            if not data:
                continue

            self.save_paper_data(data)

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
            
            self.fetch_paper_data(paper_tag)
            
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
    
            
    def read_htmls(self, to_excel = False):
        # read all html files including the subdirectories
        threads = []
        
        # create html path if it doesn't exist
        if not os.path.exists(HTML_PATH):
            os.makedirs(HTML_PATH)
            
        thread_count = 0
        file_count = 0
        
        for root, _, files in os.walk(HTML_PATH):
            for file in files:
                if not file.endswith(".html"): continue
                # create a thread for each 10 html files
                file_path = os.path.join(root, file)
                thread = threading.Thread(target=self.process_html_file, args=(file_path,))
                thread.start()
                threads.append(thread)
                
                file_count += 1
                if file_count % FILES_PER_THREAD == 0:
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
            
        # today with seconds
        today = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
        # save the cached data to a csv file
        df = pd.DataFrame(self.cached)
        
        # remove rows with null dois
        df = df[df['DOI'] != 'NULL']
        
        # remove rows with duplicated DOIs
        df.drop_duplicates(subset=['DOI'], inplace=True)
        
        # create excel, why you may ask?
        # because we need to backup before something very weird happens
        df.to_excel(os.path.join(OUTPUT_PATH, f"papers_not_scopus_wos_{today}.xlsx"), index=False)
        
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
            
        # create a new column that is called "In WOS and Scopus"
        df['WOS and Scopus'] = df.apply(lambda row: "Yes" if row['WOS'] == "Yes" and row['Scopus'] == "Yes" else "No", axis=1)
        
        # create output directory if it doesn't exist
        if not os.path.exists(OUTPUT_PATH):
            os.makedirs(OUTPUT_PATH)
            
        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # ask for user name to create a new column
        user_name = input("Introduce tu nombre y apellido: ")
        
        # create a new column with the user name and fill all the rows with the user name
        df['Scraper Responsible'] = user_name
        
        filename = f'scrape_{today}'

        if not to_excel:
            df.to_csv(os.path.join(OUTPUT_PATH, f'{filename}.csv'), index=False)
        else:
            df.to_excel(os.path.join(OUTPUT_PATH, f'{filename}.xlsx'), index=False)
            
        # create a log file
        log_file = os.path.join(OUTPUT_PATH, f'{filename}.log')
        
        with open(log_file, "w") as f:
            # describe the count of df
            f.write(f"Total papers scraped: {len(df)}\n")
            f.write(f"Total papers with DOI: {len(df[df['DOI'] != 'NULL'])}\n")
            f.write(f"Total papers without DOI: {len(df[df['DOI'] == 'NULL'])}\n")
            f.write(f"Total papers with ISSN: {len(df[df['ISSN'] != UNAVAILABLE_KEY])}\n")
            f.write(f"Total papers without ISSN: {len(df[df['ISSN'] == UNAVAILABLE_KEY])}\n")
            f.write(f"Total papers with WOS: {len(df[df['WOS'] == 'Yes'])}\n")
            # write the scraper responsible
            f.write(f"Scraper responsible: {user_name}\n")