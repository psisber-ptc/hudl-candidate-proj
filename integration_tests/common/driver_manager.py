import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from integration_tests import config

class DriverManager():
    
    _driver = None
    
    @staticmethod
    def get_driver():
        if DriverManager._driver != None:
            return DriverManager._driver
        else:
            if config.browser == "chrome":
                    _chromedriver = os.path.join(os.getcwd(), "resources", "drivers", "chromedriver")
                    if os.path.isfile(_chromedriver):
                        _service = ChromeService(executable_path=_chromedriver)
                        driver_ = webdriver.Chrome(service=_service)
                    else:
                        driver_ = webdriver.Chrome()
            elif config.browser == "firefox":
                _geckodriver = os.path.join(os.getcwd(), "resources", "drivers", "geckodriver")
                if os.path.isfile(_geckodriver):
                    _service = FirefoxService(executable_path=_geckodriver)
                    driver_ = webdriver.Firefox(service=_service)
                else:
                    driver_ = webdriver.Firefox()
            DriverManager._driver = driver_
            return DriverManager._driver
        
    @staticmethod
    def open_window(url):
        number_of_windows = len(DriverManager._driver.window_handles)
        DriverManager._driver.execute_script("window.open(arguments[0])", url)
        WebDriverWait(DriverManager._driver, 2).until(EC.number_of_windows_to_be(number_of_windows + 1))
        return DriverManager._driver.window_handles[number_of_windows]
    
    @staticmethod
    def switch_to_window_by_index(index):
        if len(DriverManager._driver.window_handles) >= index + 1:
            DriverManager._driver.switch_to.window(DriverManager._driver.window_handles[index])
            return True
        else:
            return False
    
    @staticmethod
    def switch_to_window(window):
            DriverManager._driver.switch_to.window(window)
    
    @staticmethod
    def close_window():
        if len(DriverManager._driver.window_handles) > 1:
            DriverManager._driver.close()
        else:
            DriverManager.quit_session()
            
    @staticmethod
    def quit_session():
        DriverManager._driver.quit()
        DriverManager._driver = None
            