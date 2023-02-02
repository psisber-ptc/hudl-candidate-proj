from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from integration_tests import config
from integration_tests.pages.base_page import BasePage

class RegisterSignUpEnUSPage(BasePage):
    """
    Encapsulates and abstracts all details that tests need to interact with the English US Sign Up page
    """
    
    def __init__(self, driver):
        """
        Initializes this specific page object by initializing attribute inherited from the Base page, 
        setting page specific values and defining locators needed to interact with the page.

        Args:
            driver webdriver: Shared webdriver passed in from the test
        """
        # Initialize attributes inherited from the Base page
        super(RegisterSignUpEnUSPage, self).__init__(driver)
        
        # Customize the URL for this page
        self._url = self._baseurl + "/register/signup/"
        
        # Customize the locator that is used to determine if the page has loaded
        self._page_loaded_indicator = (By.CLASS_NAME, "outer")
        
        # Dictionary of locators to be used to interact with the page.
        # Invoked by _content[locator key]. Locator is a tuple (By, selector string). Tuple is unpacked by '*'
        self._content = {
            
        }
    
    