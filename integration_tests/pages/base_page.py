from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    
    def __init__(self, driver):
        self.driver = driver
        
        self._baseurl = ""
        
        self._url = ""
        
        self._page_loaded_indicator = (By.ID, "ssr-webnav")
    
    def load(self):
        self.driver.get(self._url)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self._page_loaded_indicator))
    
    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self._page_loaded_indicator))
    
    def is_current_page(self):
        return self.driver.current_url == self._url
    
    def refresh_page(self):
        self.driver.refresh()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self._page_loaded_indicator))