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
from integration_tests.pages.login_en_us_page import LoginEnUsPage
from integration_tests.pages.home_en_us_page import HomeEnUsPage
from integration_tests.pages.login_help_en_us_page import LoginHelpEnUsPage
from integration_tests.pages.register_sign_up_en_us_page import RegisterSignUpEnUsPage

class TestLoginEnPage():
    
    valid_invalid_creds_testdata = [
        ("Invalid password test", user_creds.email, "invalid-password", False),
        ("Invalid email test", "invalid-email@bad-domain.com", user_creds.password, False),
        ("Valid credentails test", user_creds.email, user_creds.password, True),
        ("Case sensitive password test1", user_creds.email, user_creds.password.lower(), False),
        ("Case sensitive password test2", user_creds.email, user_creds.password.upper(), False),
        ("Case insensitive email test", user_creds.email.upper(), user_creds.password, True),
        ("Mismatched valid user and valid password", "tyler.puccio@hudl.com", user_creds.password, False)
    ]
    
    @pytest.mark.parametrize("test_case, email, password, expected_result", valid_invalid_creds_testdata)
    def test_valid_and_invalid_credentials(self, driver, test_case, email, password, expected_result):
        
        login_page = LoginEnUsPage(driver)
        home_page = HomeEnUsPage(driver)
        login_page.load()
        login_page.login_with_email_and_password(email, password)
        if login_page.login_failed():
            assert expected_result == False
        else:
            home_page.wait_for_page_to_load(2)        
            assert home_page.is_current_page()
        
    def test_login_help_link(self, driver):
        
        login_page = LoginEnUsPage(driver)
        login_help_page = LoginHelpEnUsPage(driver)
        login_page.load()
        login_page.need_help()
        login_help_page.wait_for_page_to_load(2)
        assert login_help_page.is_current_page()
    
    def test_sign_up_link(self, driver):
        
        login_page = LoginEnUsPage(driver)
        register_sign_up_en_page = RegisterSignUpEnUsPage(driver)
        login_page.load()
        login_page.sign_up()
        register_sign_up_en_page.wait_for_page_to_load(2)
        assert register_sign_up_en_page.is_current_page()
    
        