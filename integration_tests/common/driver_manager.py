import os
import pickle

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from integration_tests import config

class DriverManager():
    
    """
    Class to centrally manage a single webdriver instance and associated functions.

    """
    
    # Static variable the maintains the 'master' copy of the webdriver.
    _driver = None
    
    @staticmethod
    def get_driver():
        
        """
        Instantiates a webdriver for the applicable browser according to a value in config.py. 
        Value in config.py is set in conftest.py from a custom command line argument --browsername which defaulst to chrome.
        Command line arguments are defined in conftest.py.
        Returns:
            webdriver: webdriver for the applicable browser
        """
        # If the webdriver already exists, return it.
        if DriverManager._driver != None:
            return DriverManager._driver
        #Otherwise instantiate the driver, save it in the static variable and return it.
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
        """
        Opens a new window browser window for the specified URL. It return the handle for the new window
        Note:  It does not switch to the new window.

        Args:
            url ste: URL of page to open in new browser window

        Returns:
            _type_: _description_
        """
        # Get the current number of windows
        number_of_windows = len(DriverManager._driver.window_handles)
        # Execute javascrip to open a new window at the specified URL. the variable url is passed to the script as argument[0]
        DriverManager._driver.execute_script("window.open(arguments[0])", url)
        # Wait for the number of windows to be incremented
        WebDriverWait(DriverManager._driver, 2).until(EC.number_of_windows_to_be(number_of_windows + 1))
        # Number of windows is now the index of the new window handle
        return DriverManager._driver.window_handles[number_of_windows]
    
    @staticmethod
    def switch_to_window_by_index(index):
        """
        Switches to the window at the specified index in the list of window handles.

        Args:
            index int: Index in the list of window handles of the window to switch to

        Returns:
            bool: True if new window was opened successfully. False otherwise.
        """
        # The number of window handles is greater than or equal to the index, switch to the window and report success = True
        if len(DriverManager._driver.window_handles) >= index + 1:
            DriverManager._driver.switch_to.window(DriverManager._driver.window_handles[index])
            return True
        # Otherwise do nothing and return success = False
        else:
            return False
    
    @staticmethod
    def switch_to_window(window_handle):
        
        """
        Switches to the window specified by the window handle.
        
        Args:
            window_handle str: Handle of window handles of the window to switch to

        """
        DriverManager._driver.switch_to.window(window_handle)
    
    @staticmethod
    def save_cookies():
        
        """
        Saves cookies as the binary file 'hudl_test_cookies' in an attempt to save state between webdriver instances.
        
        TODO: Determine why this is not able to persist 'Remember me' state in conjunction with restore_cookies()
        """
        # Uses the python pickle module
        pickle.dump(DriverManager._driver.get_cookies(), open("hudl_test_cookies.pkl", "wb"))
    
    @staticmethod
    def restore_cookies():
        
        """
        Restores cookies from the binary file 'hudl_test_cookies' in an attempt to save state between webdriver instances.
        
        TODO: Determine why this is not able to persist 'Remember me' state in conjunction with save_cookies()
        """
        # Uses python pickle module
        hudl_test_cookies = pickle.load(open("hudl_test_cookies.pkl", "rb"))
        for hudl_test_cookie in hudl_test_cookies:
            DriverManager._driver.add_cookie(hudl_test_cookie)
    
    @staticmethod
    def close_window():
        """
        Closes the current window. If the current window is the only window open it ends the session and disposes of the driver and resets _driver to None using quit_session().
        """
        # 
        if len(DriverManager._driver.window_handles) > 1:
            DriverManager._driver.close()
        else:
            DriverManager.quit_session()
            
    @staticmethod
    def quit_session():
        
        """
        Closes all windows, ends the session, disposes of the driver and resets _driver to None.
        """
        
        DriverManager._driver.quit()
        DriverManager._driver = None
            