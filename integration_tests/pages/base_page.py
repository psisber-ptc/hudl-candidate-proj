from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from integration_tests import config
from integration_tests.common.driver_manager import DriverManager

class BasePage():
    
    def __init__(self, driver):
        self.driver = driver
        
        self._baseurl = config.baseurl
        
        self._url = ""
        
        self._page_loaded_indicator = (By.ID, "ssr-webnav")
    
    def load(self):
        self.driver.get(self._url)
    
    def wait_for_page_to_load(self, timeout):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self._page_loaded_indicator))
    
    def is_current_page(self):
        return self.driver.current_url in self._url
    
    def _is_displayed(self, locator, timeout=0):
        if timeout > 0:
            try:
                WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self.driver.find_element(*locator)
            except NoSuchElementException:
                return False
    
    def refresh(self):
        self.driver.refresh()
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(self._page_loaded_indicator))
    
    def _click_blocked_element(self, element):
        ActionChains(self.driver).move_to_element(element).click(element).perform()
    
    def _click_dropdown_item(self, dropdown, item):
        ActionChains(self.driver).move_to_element(dropdown).click(item).perform()