import pytest
import os
# import re
# import requests
# import urlib
# import datetime
# from dateparser.search import search_dates
# from bs4 import BeautifulSoup
# import glob as glob
from time import sleep

from integration_tests import user_creds
from integration_tests.common.driver_manager import DriverManager
from integration_tests.pages.login_en_us_page import LoginEnUSPage
from integration_tests.pages.home_en_us_page import HomeEnUSPage
from integration_tests.pages.login_help_en_us_page import LoginHelpEnUSPage
from integration_tests.pages.register_sign_up_en_us_page import RegisterSignUpEnUSPage
from integration_tests.pages.landing_en_us_page import LandingEnUSPage

class TestLoginEnUSPage():
    
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
        login_page = LoginEnUSPage(driver)
        home_page = HomeEnUSPage(driver)
        login_page.load()
        login_page.login_with_email_and_password(email, password)
        if login_page.login_failed():
            assert expected_result == False
        else:
            home_page.wait_for_page_to_load(2)        
            assert home_page.is_current_page()
        
    def test_login_help_link(self, driver):
        login_page = LoginEnUSPage(driver)
        login_help_page = LoginHelpEnUSPage(driver)
        login_page.load()
        login_page.need_help()
        login_help_page.wait_for_page_to_load(2)
        assert login_help_page.is_current_page()
    
    def test_sign_up_link(self, driver):
        login_page = LoginEnUSPage(driver)
        register_sign_up_us_page = RegisterSignUpEnUSPage(driver)
        login_page.load()
        login_page.sign_up()
        register_sign_up_us_page.wait_for_page_to_load(2)
        assert register_sign_up_us_page.is_current_page()
    
    def test_logout(self, driver):
        login_page = LoginEnUSPage(driver)
        home_page = HomeEnUSPage(driver)
        landing_page = LandingEnUSPage(driver)
        login_page.load()
        login_page.dont_remember_me()
        login_page.login()
        home_page.wait_for_page_to_load(2)
        home_page.logout()
        landing_page.wait_for_page_to_load(2)
        assert landing_page.is_current_page()
        DriverManager.quit_session()
        new_driver = DriverManager.get_driver()
        new_landing_page = LandingEnUSPage(new_driver)
        new_landing_page.load()
        new_landing_page.wait_for_page_to_load(2)
        assert new_landing_page.is_current_page()
    
    def test_logout_with_remember_me(self, driver):
        login_page = LoginEnUSPage(driver)
        home_page = HomeEnUSPage(driver)
        landing_page = LandingEnUSPage(driver)
        login_page.load()
        login_page.remember_me()
        login_page.login()
        home_page.wait_for_page_to_load(2)
        home_page.logout()
        landing_page.wait_for_page_to_load(2)
        DriverManager.quit_session()
        new_driver = DriverManager.get_driver()
        new_landing_page = LandingEnUSPage(new_driver)
        new_landing_page.load()
        new_landing_page.wait_for_page_to_load(2)
        assert new_landing_page.is_current_page()
    
    def test_close_window_keep_session(self, driver):
        login_page = LoginEnUSPage(driver)
        home_page = HomeEnUSPage(driver)
        landing_page = LandingEnUSPage(driver)
        login_page.load()
        login_page.dont_remember_me()
        login_page.login()
        home_page.wait_for_page_to_load(2)
        primary_window = driver.window_handles[0]
        secondary_window = DriverManager.open_window("https://www.google.com/")
        DriverManager.switch_to_window(secondary_window)
        sleep(2)
        DriverManager.switch_to_window(primary_window)
        sleep(2)
        DriverManager.close_window()
        DriverManager.switch_to_window(secondary_window)
        landing_page.load()
        home_page.wait_for_page_to_load(5)
        assert home_page.is_current_page()
    
    def test_close_window_keep_session_with_remember_me(self, driver):
        login_page = LoginEnUSPage(driver)
        home_page = HomeEnUSPage(driver)
        landing_page = LandingEnUSPage(driver)
        login_page.load()
        login_page.remember_me()
        login_page.login()
        home_page.wait_for_page_to_load(2)
        primary_window = driver.window_handles[0]
        secondary_window = DriverManager.open_window("https://www.google.com/")
        DriverManager.switch_to_window(secondary_window)
        sleep(2)
        DriverManager.switch_to_window(primary_window)
        sleep(2)
        DriverManager.close_window()
        DriverManager.switch_to_window(secondary_window)
        landing_page.load()
        home_page.wait_for_page_to_load(5)
        assert home_page.is_current_page()
    