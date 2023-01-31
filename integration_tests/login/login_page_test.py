import pytest
import os
# import re
# import requests
# import urlib
# import datetime
# from dateparser.search import search_dates
# from bs4 import BeautifulSoup
# import glob as glob
# from time import sleep

from integration_tests import user_creds
from integration_tests.pages.login_page import LoginPage
from integration_tests.pages.home_page import HomePage
from integration_tests.pages.login_help_page import LoginHelpPage

class TestLoginPage():
    
    valid_invalid_creds_testdata = [
        ("Invalid password test", user_creds.email, "invalid-password", False),
        ("Invalid email test", "invalid-email@bad-domain.com", user_creds.password, False),
        ("Valid credentails test", user_creds.email, user_creds.password, True)
    ]
    
    @pytest.mark.parametrize("test_case, email, password, expected_result", valid_invalid_creds_testdata)
    def test_valid_and_invalid_credentials(self, driver, test_case, email, password, expected_result):
        
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        login_page.load()
        login_page.login_with_email_and_password(email, password)
        if login_page.login_failed():
            assert expected_result == False
        else:
            home_page.wait_for_page_to_load(2)        
            assert home_page.is_current_page()
        
    def test_login_help_link(self, driver):
        
        login_page = LoginPage(driver)
        login_help_page = LoginHelpPage(driver)
        login_page.load()
        login_page.need_help()
        login_help_page.wait_for_page_to_load(2)
        assert login_help_page.is_current_page()
        