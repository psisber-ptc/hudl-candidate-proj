from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from integration_tests import config
from integration_tests import user_creds
from integration_tests.pages.base_page import BasePage

class LoginEnUSPage(BasePage):
    
    def __init__(self, driver):
        super(LoginEnUSPage, self).__init__(driver)
        
        self._url = self._baseurl + "/login/"
        
        self._page_loaded_indicator = (By.ID, "app")
        
        self._content = {
                            "email_field": (By.ID, "email"),
                            "password_field": (By.ID, "password"),
                            "login_button": (By.CSS_SELECTOR, "button"),
                            "remember_me": (By.CSS_SELECTOR, "input[data-qa-id='remember-me-checkbox']"),
                            "remember_me_unchecked": (By.CSS_SELECTOR, "div[class^='uni-form__check-item']:not([class$='is-checked'])"),
                            "remember_me_checked": (By.CSS_SELECTOR, "div[class^='uni-form__check-item'][class$='is-checked']"),
                            "need_help": (By.CSS_SELECTOR, "a[data-qa-id='need-help-link']"),
                            "sign_up": (By.CSS_SELECTOR, "a[class*='signUpLink']"),
                            "login_failed_message": (By.CSS_SELECTOR, "*[data-qa-id='error-display']")
                            }
    
    def login_with_email_and_password(self, email, password):
        self.driver.find_element(*(self._content["email_field"])).send_keys(email)
        self.driver.find_element(*(self._content["password_field"])).send_keys(password)
        self.driver.find_element(*(self._content["login_button"])).click()
    
    def login(self):
        self.login_with_email_and_password(user_creds.email, user_creds.password)
    
    
    def need_help(self):
        self.driver.find_element(*(self._content["need_help"])).click()
    
    def remember_me(self):
        if self.driver.find_element(*(self._content["remember_me_unchecked"])).is_displayed():
            _check_box = self.driver.find_element(*(self._content["remember_me"]))
            self._click_blocked_element(_check_box)
        elif self.driver.find_element(*(self._content["remember_me_checked"])).is_displayed():
            return
    
    def dont_remember_me(self):
        if self.driver.find_element(*(self._content["remember_me_unchecked"])).is_displayed():
            return
        elif self.driver.find_element(*(self._content["remember_me_checked"])):
            _check_box = self.driver.find_element(*(self._content["remember_me"]))
            self._click_blocked_element(_check_box)
    
    def sign_up(self):
        self.driver.find_element(*(self._content["sign_up"])).click()
    
    def login_failed(self):
        return self._is_displayed(self._content["login_failed_message"], 2)
    
    
    