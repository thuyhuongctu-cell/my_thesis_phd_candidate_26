import requests
import os
import subprocess
import shutil

from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

BASE_DOMAIN = "https://portableapps.com"

FILE_DIR = os.path.dirname(os.path.realpath(__file__))
TEMP_DIR = os.path.join(FILE_DIR, "temp")
BROWSER_DIR = os.path.join(FILE_DIR, "browser")

FIREFOX_PORTABLE = "FirefoxPortable"
FIREFOX64_VERSION_PATH = os.path.join(BROWSER_DIR, FIREFOX_PORTABLE, "App", "Firefox64", "firefox.exe")
FIREFOX_PROFILE_PATH = os.path.join(BROWSER_DIR, FIREFOX_PORTABLE, "Data", "profile")

BUFFER_SIZE = 1024

# FIREFOX_PAF = BASE_DOMAIN + "/apps/internet/firefox_portable"

class FirefoxPortableDownloader:
    FIREFOX_PAF = BASE_DOMAIN + "/apps/internet/firefox_portable"

    def __init__(self):
        self.paf_session = requests.Session()
        self.last_file = ""
        
    def is_firefox_portable_installed(self):
        return os.path.exists(os.path.join(BROWSER_DIR, FIREFOX_PORTABLE))

    def __explore(self, url):
        data = self.paf_session.get(url)
        soup = BeautifulSoup(data.text, "lxml")
        return soup
    
    def __get_exe_link(self):
        firefox_home = self.__explore(self.FIREFOX_PAF)
        box_download = firefox_home.find("div", {"class": "download-box"})
        download_link = box_download.find("a")["href"]
        
        download_page = self.__explore(BASE_DOMAIN + download_link)
        
        div_data = download_page.find("div", {"class": "field-item even"})
        
        # get all links
        all_links = div_data.find_all("a")

        # search if it has /redir2/ in the link
        for link in all_links:
            print(link.get("href"))
            if "/redir2/" in link["href"]:
                download_link = BASE_DOMAIN + link["href"]
                break
            
        return download_link
    
    def download(self):
        download_link = self.__get_exe_link()
        exe = self.paf_session.get(download_link, stream=True)
        
        # create temp directory if not exists
        if not os.path.exists(TEMP_DIR):
            os.makedirs(TEMP_DIR)
            
        print("Downloading Firefox Portable")
        
        # make progress bar
        total_length = int(exe.headers.get('content-length'))
        
        parsed_url = urlparse(download_link)
        query_params = parse_qs(parsed_url.query)
        filename = query_params['f'][0]        
        
        # dowmload the file by chunks
        with open(os.path.join(TEMP_DIR, filename), "wb") as f:
            progress_bar = tqdm(total=total_length, unit="B", unit_scale=True)
            for chunk in exe.iter_content(chunk_size=BUFFER_SIZE):
                if chunk:
                    f.write(chunk)
                    progress_bar.update(len(chunk))
                    
        self.last_file = filename
                    
    def run_installer(self):
        # call from MDI directory
        subprocess.run([os.path.join(TEMP_DIR, self.last_file)], cwd=os.path.join(FILE_DIR))
        
    def setup(self):
        self.download()
        print("Running installer...")
        self.run_installer()
        self.cleanup()
        
    def cleanup(self):
        # check if FirefoxPortable is on temp directory and move it to BROWSER_DIR
        if not os.path.exists(BROWSER_DIR):
            os.makedirs(BROWSER_DIR)
            
        if os.path.exists(os.path.join(TEMP_DIR, FIREFOX_PORTABLE)):
            shutil.move(os.path.join(TEMP_DIR, FIREFOX_PORTABLE), BROWSER_DIR)
        else:
            print("FirefoxPortable was removed aborting!!!")
        
        if os.path.exists(TEMP_DIR):
            shutil.rmtree(TEMP_DIR)
        
            
        
        
