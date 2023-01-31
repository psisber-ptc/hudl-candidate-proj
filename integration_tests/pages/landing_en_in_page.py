from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from integration_tests import config
from integration_tests.pages.base_page import BasePage

class LandingEnInPage(BasePage):
    
    def __init__(self, driver):
        super(LandingEnInPage, self).__init__(driver)
        
        self._url = self._baseurl + "/en_gb/"
        
        self._page_loaded_indicator = (By.CLASS_NAME, "outer")
        
        self._content = {
            "language_selector": (By.ID, "l10n-selector__options"),
            "log_in_button": (By.CSS_SELECTOR, "a[data-qa-id='login']"),
            "contact_us_button": (By.CSS_SELECTOR, "a[class$='btn--secondary']")
        }
    