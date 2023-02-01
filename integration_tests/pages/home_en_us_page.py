from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from integration_tests import config
from integration_tests.pages.base_page import BasePage

class HomeEnUSPage(BasePage):
    
    def __init__(self, driver):
        super(HomeEnUSPage, self).__init__(driver)
        
        self._url = self._baseurl + "/home/"
        
        # self._page_loaded_indicator = (By.CSS_SELECTOR, "div[class$='home logged-in']")
        
        self._content = {
            "user_menu_dropdown": (By.CLASS_NAME, "hui-globaluseritem"),
            "logout": (By.CSS_SELECTOR, "*[data-qa-id='webnav-usermenu-logout']")
        }
    
    def logout(self):
        dropdown = self.driver.find_element(*(self._content["user_menu_dropdown"]))
        item = self.driver.find_element(*(self._content["logout"]))
        self._click_dropdown_item(dropdown, item)
    