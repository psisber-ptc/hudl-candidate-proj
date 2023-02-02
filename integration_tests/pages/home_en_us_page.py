from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from integration_tests import config
from integration_tests.pages.base_page import BasePage

class HomeEnUSPage(BasePage):
    
    """
    Encapsulates and abstracts all details that tests need to interact with the English US Home page
    """
    
    def __init__(self, driver):
        """
        Initializes this specific page object by initializing attribute inherited from the Base page, 
        setting page specific values and defining locators needed to interact with the page.

        Args:
            driver webdriver: Shared webdriver passed in from the test
        """
        # Initialize attributes inherited from the Base page
        super(HomeEnUSPage, self).__init__(driver)
        
        # Customize the URL for this page
        self._url = self._baseurl + "/home/"
        
        # Uses default value specified in Base page
        # This is an alternate selector more specific to this page if needed
        # self._page_loaded_indicator = (By.CSS_SELECTOR, "div[class$='home logged-in']")
        
        # Dictionary of locators to be used to interact with the page.
        # Invoked by _content[locator key]. Locator is a tuple (By, selector string). Tuple is unpacked by '*'
        self._content = {
            "user_menu_dropdown": (By.CLASS_NAME, "hui-globaluseritem"),
            "logout": (By.CSS_SELECTOR, "*[data-qa-id='webnav-usermenu-logout']")
        }
    
    def logout(self):
        """
        Invoked by tests to log out
        Uses helper method _click_dropdown_item() from Base page to get around issues clicking the dropdown item (mouse over on parent required)
        """
        dropdown = self.driver.find_element(*(self._content["user_menu_dropdown"]))
        item = self.driver.find_element(*(self._content["logout"]))
        self._click_dropdown_item(dropdown, item)
    