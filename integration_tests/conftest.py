import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from integration_tests import config

def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action = "store",
                     default = "https://www.hudl.com",
                     help = "Base URL for the application under test")

@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption("--baseurl")
    _chromedriver_rel_path = os.path.join("resources", "chromedriver")
    _chromedriver = os.path.join(os.path.dirname(os.getcwd()), _chromedriver_rel_path)
    if os.path.isfile(_chromedriver):
        _service = ChromeService(executable_path=_chromedriver)
        driver_ = webdriver.Chrome(service=_service)
    else:
        driver_ = webdriver.Chrome()
    
    def quit():
        driver_.quit()
    
    request.addfinalizer(quit)
    
    return driver_