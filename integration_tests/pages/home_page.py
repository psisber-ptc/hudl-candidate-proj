from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config
from pages.base_page import BasePage

class HomePage(BasePage):
    
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        
        self._baseurl = config.baseurl
        
        self._url = self._baseurl + "/home"
        print(f"\n***** URL:  {self._url}")
        
        self._content = {}
    