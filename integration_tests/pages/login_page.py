from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from integration_tests import config
from integration_tests.pages.base_page import BasePage

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        
        self._url = self._baseurl + "/login"
        
        self._page_loaded_indicator = (By.ID, "app")
        
        self._content = {
                            "email_field": (By.ID, "email"),
                            "password_field": (By.ID, "password"),
                            "login_button": (By.CSS_SELECTOR, "button"),
                            "need_help": (By.CSS_SELECTOR, "a[data-qa-id='need-help-link']"),
                            "login_failed_message": (By.CSS_SELECTOR, "*[data-qa-id='error-display']")
                            }
    
    def login_with_email_and_password(self, email, password):
        self.driver.find_element(*(self._content["email_field"])).send_keys(email)
        self.driver.find_element(*(self._content["password_field"])).send_keys(password)
        self.driver.find_element(*(self._content["login_button"])).click()
    
    def need_help(self):
        self.driver.find_element(*(self._content["need_help"])).click()
    
    def login_failed(self):
        return self._is_displayed(self._content["login_failed_message"], 2)
    