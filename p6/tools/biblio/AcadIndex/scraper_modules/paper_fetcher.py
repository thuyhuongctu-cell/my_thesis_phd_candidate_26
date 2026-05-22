
from time import sleep
import queue
import threading

from .wos_multiprocess import UNAVAILABLE_KEY
from .crossref_wrapper import CrossrefWrapper
from .title_matcher import TitleMatcher

MAX_RETRIES = 3

PAPER_DATA_KEYS = [
    'Title', 
    'Author', 
    'Year', 
    'DOI', 
    'Publisher', 
    'URL', 
    'Reference Count', 
    'Times Referenced', 
    'ISSN',
    'Type'
]

# this is because the problem of rate limiting.
ACCEPTABLE_THREAD_COUNT = 4

class MultiPaperFetcher:
    def __init__(self, similarity_threshold : float, thread_count : int = ACCEPTABLE_THREAD_COUNT) -> None:
        self.cr_wrapper = CrossrefWrapper()
        self.__thread_count = thread_count
        self.similarity_threshold = similarity_threshold
        
        # REFERENCE!!!!
        self.cached_papers = {key : [] for key in PAPER_DATA_KEYS}
        
        # mismatch log
        self.mismatched_titles = {
            # key is the real title, value is the mismatched title
        }
        
        self.unfetched_titles = []
        
    def set_thread_count(self, thread_count : int):
        self.__thread_count = thread_count
    
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
    
    def __save_paper_data(self, data : dict):
        for key in PAPER_DATA_KEYS:
            self.cached_papers[key].append(data[key])
            
    def __internal_save_paper_data(self, title : str):
        items = self.fetch_data(title)
        if not items:
            return
        
        data = self.extract_data(items)
        
        if not data:
            return
        
        self.__save_paper_data(data)
    
    def __internal_thread_fetch(self, titles_queue : queue.Queue):
        while not titles_queue.empty():
            title = titles_queue.get()
            try:
                self.__internal_save_paper_data(title)
                # Respectful delay to avoid rate limit
                sleep(1)  # Adjust this delay based on your observed rate limit behavior
            except Exception as e:
                print(f"Error fetching data for title {title}: {e}")
            finally:
                titles_queue.task_done()
                print("Remaining tasks: ", titles_queue.qsize())
                
        print("Thread finished.")
    
    def fetch_papers_data(self, paper_names: list[str]) -> list[dict]:
        titles_queue = queue.Queue()

        for paper_name in paper_names:
            titles_queue.put(paper_name)
            
        # create a list of threads
        threads = []
        
        for i in range(self.__thread_count):
            thread = threading.Thread(target=self.__internal_thread_fetch, args=(titles_queue,))
            thread.start()
            threads.append(thread)
            
        thread: threading.Thread
        for thread in threads:
            thread.join()
            
        return self.cached_papers
        
    def fetch_data(self, papername: str, retries: int = MAX_RETRIES) -> dict | None:
        print("Obteniendo datos del paper ", papername)

        for attempt in range(retries):
            try:
                paper_data = self.retry_works(papername)
                message = paper_data.get('message')

                if not message:
                    return None

                items = message['items']
                best_match = None
                highest_similarity = 0

                # Check if any item matches the paper name
                for item in items:
                    item_title = item.get('title')

                    if not item_title:
                        # print("Invalid title for item: ", item, "papername: ", papername)
                        continue

                    item_title = item_title[0]
                    
                    # First, try exact match (case-insensitive)
                    if item_title.lower() == papername.lower():
                        return item
                    
                    # If no exact match, calculate similarity
                    similarity = TitleMatcher.calculate_similarity(item_title, papername)
                    if similarity > highest_similarity:
                        highest_similarity = similarity
                        best_match = item
    
                if highest_similarity >= self.similarity_threshold:
                    return best_match

                # Log the mismatch
                if items:
                    print(f"NOT FOUND: {papername}")
                    print(f"BEST MATCH: {items[0]['title'][0]} (similarity: {highest_similarity:.2f})")
                    
                    self.mismatched_titles[papername] = items[0]['title'][0]
                    
                # save it anyways because even if it doesn't match, it might be useful
                self.unfetched_titles.append(papername)
                
                return items[0]

            except Exception as e:
                print(f"An error occurred while fetching data for {papername}: {e}")

                if attempt < retries - 1:
                    print(f"Retrying after {2 ** attempt} seconds...")
                    sleep(2 ** attempt)
                else:
                    self.unfetched_titles.append(papername)
                    print(f"All {retries} attempts failed. Unable to fetch data for {papername}.")
                    return None

    def retry_works(self, papername: str):
        for attempt in range(MAX_RETRIES):  # Retry 3 times
            try:
                paper_data = self.cr_wrapper.search_by_title(papername)
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
        
        all_authors = item.get('author')
        
        # we don't care about invalid authors
        # edit: yes we care
        author = "NOT FOUND"
        
        if all_authors:
             # save all authors separated by comma
            authors = []
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
        # print(ref_count, times_referenced)
        
        doi = item['DOI']
        publisher = item['publisher']
        
        # get url
        url = item['resource']['primary']['URL']
        
        # get issn, also its possible that some papers may not have an issn
        issn = self.__get_proper_issn(item)
        
        elem_type = item.get('type')
        
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
            'ISSN' : issn,
            'Type' : elem_type
        }