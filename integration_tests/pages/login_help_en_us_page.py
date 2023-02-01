from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from integration_tests import config
from integration_tests.pages.base_page import BasePage

class LoginHelpEnUSPage(BasePage):
    
    def __init__(self, driver):
        super(LoginHelpEnUSPage, self).__init__(driver)
        
        self._url = self._baseurl + "/login/help#"
        
        self._page_loaded_indicator = (By.ID, "app")
        
        self._content = {
                            "email_field": (By.CSS_SELECTOR, "input[data-qa-id='password-reset-input']"),
                            "send_passwrod_reset_button_enabled": (By.CSS_SELECTOR, "button[data-qa-id='password-reset-submit-btn']:not([disabled])"),
                            "send_passwrod_reset_button_enabled": (By.CSS_SELECTOR, "button[data-qa-id='password-reset-submit-btn'][disabled]")
                            }
    
    