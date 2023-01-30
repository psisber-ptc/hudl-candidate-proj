from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config
from pages.base_page import BasePage

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        
        self._baseurl = config.baseurl
        
        self._url = self._baseurl + "/login"
        print(f"\n***** URL:  {self._url}")
        
        self._page_loaded_indicator = (By.ID, "app")
        
        self._content = {
                            "email_field": (By.ID, "email"),
                            "password_field": (By.ID, "password"),
                            "login_button": (By.CSS_SELECTOR, "button")
                            }
    
    def login_with_email_and_password(self, email, password):
        self.driver.find_element(*(self._content["email_field"])).send_keys(email)
        self.driver.find_element(*(self._content["password_field"])).send_keys(password)
        self.driver.find_element(*(self._content["login_button"])).click()
    