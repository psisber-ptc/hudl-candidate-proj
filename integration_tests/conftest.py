import pytest
import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from integration_tests import config

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
    
    def quit():
        driver_.quit()
    
    request.addfinalizer(quit)
    
    return driver_