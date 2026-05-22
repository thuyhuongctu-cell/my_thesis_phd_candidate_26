from scraper_modules.parser_scholar_singlethread import ParserScholarLite
import time
import os

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
QUERIES_PATH = os.path.join(FILE_PATH, "queries")

print("[INFO] Initializing ParserScholar...")

if __name__ == "__main__":
    # benchmark time
    start = time.time()
    
    # iterate every folder in the queries folder
    for folder in os.listdir(QUERIES_PATH):
        # get the path
        path = os.path.join(QUERIES_PATH, folder)
        
        # if the path is a directory
        if os.path.isdir(path):
            # create a new parser
            scraper = ParserScholarLite(use_wos_api=True, use_indexers=False)
            # read the htmls
            scraper.read_htmls(to_excel=True, path=path)

    end = time.time()
    
    # print the time taken
    print(f"[INFO] Time taken: {end - start} seconds.")