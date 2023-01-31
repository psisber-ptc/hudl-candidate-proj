from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from integration_tests import config
from integration_tests.pages.base_page import BasePage

class LandingEsPage(BasePage):
    
    def __init__(self, driver):
        super(LandingEsPage, self).__init__(driver)
        
        self._url = "es." + self._baseurl +"/es-xl"
        
        self._page_loaded_indicator = (By.ID, "__gatsby")
        
        self._content = {
            "language_selector": (By.ID, "l10n-selector__options"),
            "request_demo_button": (By.CSS_SELECTOR, "a[class$='primary-button-dark']")
        }
    