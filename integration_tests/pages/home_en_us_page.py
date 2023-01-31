from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from integration_tests import config
from integration_tests.pages.base_page import BasePage

class HomeEnUsPage(BasePage):
    
    def __init__(self, driver):
        super(HomeEnUsPage, self).__init__(driver)
        
        self._url = self._baseurl + "/home"
        
        self._content = {}
    