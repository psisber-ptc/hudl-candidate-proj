import pytest
import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from integration_tests import config
from integration_tests.common.driver_manager import DriverManager

def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action = "store",
                     default = "https://www.hudl.com",
                     help = "Base URL for the application under test")
    parser.addoption("--browser",
                      action = "store",
                      default = "chrome",
                      help = "The name of the browser to test with"
                      )

@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption("--baseurl")
    config.browser = request.config.getoption("--browser").lower()
    
    driver_ = DriverManager.get_driver()
    
    def quit():
        DriverManager.quit_session()
    
    request.addfinalizer(quit)
    
    return driver_