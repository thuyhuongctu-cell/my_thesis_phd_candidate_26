from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedTagNameException

# wrapper only for Firefox because we have portable one
class SimpleFirefox:
    def __init__(self, profile_path : str, binary_path : str, headless : bool = True):
        self.profile_path = profile_path
        self.binary_path = binary_path
        self.headless = headless
    
    def __setup(self) -> webdriver.FirefoxOptions | webdriver.FirefoxProfile:
        options = webdriver.FirefoxOptions()
        profile = webdriver.FirefoxProfile(self.profile_path)
        options.profile = profile
        options.binary_location = self.binary_path
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        
        self.__options = options

    def instance(self):
        self.__setup()
        return webdriver.Firefox(options=self.__options)
        
    
        