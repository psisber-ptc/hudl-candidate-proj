from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from integration_tests import config
from integration_tests.pages.base_page import BasePage

class RegisterSignUpEnUSPage(BasePage):
    
    def __init__(self, driver):
        super(RegisterSignUpEnUSPage, self).__init__(driver)
        
        self._url = self._baseurl + "/register/signup/"
        
        self._page_loaded_indicator = (By.CLASS_NAME, "outer")
        
        self._content = {}
    
    