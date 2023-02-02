import pytest

# ***** Some common imports for easy reference
# import os
# import re
# import requests
# import urlib
# import datetime
# from dateparser.search import search_dates
# from bs4 import BeautifulSoup
# import glob as glob
# from time import sleep
# ***************************************************

from integration_tests import user_creds
from integration_tests.common.driver_manager import DriverManager
from integration_tests.pages.login_en_us_page import LoginEnUSPage
from integration_tests.pages.home_en_us_page import HomeEnUSPage
from integration_tests.pages.login_help_en_us_page import LoginHelpEnUSPage
from integration_tests.pages.register_sign_up_en_us_page import RegisterSignUpEnUSPage
from integration_tests.pages.landing_en_us_page import LandingEnUSPage

class TestLoginEnUSPage():
    
    """Tests for the Englis US Login page including some tests of logout from the Home page because they make sense here."""
    
    # Testdata section
    
    # Testdata for login tests with various valid and invalid credentails
    valid_invalid_creds_testdata = [
        ("Invalid password test", user_creds.email, "invalid-password", False),
        ("Invalid email test", "invalid-email@bad-domain.com", user_creds.password, False),
        ("Valid credentails test", user_creds.email, user_creds.password, True),
        ("Case sensitive password test1", user_creds.email, user_creds.password.lower(), False),
        ("Case sensitive password test2", user_creds.email, user_creds.password.upper(), False),
        ("Case insensitive email test", user_creds.email.upper(), user_creds.password, True),
        ("Mismatched valid user and valid password", "tyler.puccio@hudl.com", user_creds.password, False)
    ]
    
    # Testdata for tests that need to run with and without 'Remember me' selected
    remember_me_testdata = [
        ("Remember me NOT selected", False),
        ("Remember me selected", True),
    ]
    
    @pytest.mark.parametrize("test_case, email, password, expected_result", valid_invalid_creds_testdata)
    def test_login_with_valid_and_invalid_credentials(self, driver, test_case, email, password, expected_result):
        
        """
        Test that verifies logging in with various valid and invalid credentials. This is a data-driven test.
        """
        
        # Set up the Login page and Home page instances
        login_page = LoginEnUSPage(driver)
        home_page = HomeEnUSPage(driver)
        
        # Go directly to the Login page (skips Landing page because it is not being tested in these tests)
        login_page.load()
        
        # Attempt to log in with credentials for the current testcase (as parametrized with applicable testdata)
        login_page.login_with_email_and_password(email, password)
        
        # If the login fails and failure was expected per the testdata the test passes
        # If the login fails and failure was NOT expected per the testdata the test fails
        if login_page.login_failed():
            assert expected_result == False
        # If the login succeeds and success was expected per the testdata the test passes
        # If the login succeeds and success was NOT expected per the testdata the test fails
        # The expected result of a successful login is the Home page
        else:
            home_page.wait_for_page_to_load(5)
            assert expected_result == True
            assert home_page.is_current_page()
        
    def test_login_help_link(self, driver):
        
        """Test that verifies the 'Need Help?' link"""
        
        # Set up the Login page and Help page instances
        login_page = LoginEnUSPage(driver)
        login_help_page = LoginHelpEnUSPage(driver)
        
        # Go directly to the Login page (skips Landing page because it is not being tested in these tests)
        login_page.load()
        
        # Attempt to access the login help
        login_page.need_help()
        
        # The expected result is the Login Help page
        login_help_page.wait_for_page_to_load(5)
        assert login_help_page.is_current_page()
    
    def test_sign_up_link(self, driver):
        
        """
        Test that verifies the 'Sign up' link
        """
        
        # Set up the Login page and Register/Sign Up page instances
        login_page = LoginEnUSPage(driver)
        register_sign_up_us_page = RegisterSignUpEnUSPage(driver)
        
        # Go directly to the Login page (skips Landing page because it is not being tested in these tests)
        login_page.load()
        
        # Attempt to access the Sign Up page
        login_page.sign_up()
        
        # The expected result is the Sign Up page
        register_sign_up_us_page.wait_for_page_to_load(5)
        assert register_sign_up_us_page.is_current_page()
    
    @pytest.mark.parametrize("test_case, remember_me", remember_me_testdata)
    def test_logout_without_and_with_remember_me(self, driver, test_case, remember_me):
        
        """
        Test that verifies logout from the Home page without and with 'Remember me' selected.
        This is a data-driven test.
        """
        
        # Set up the Login page, Home page and Landing page instances
        login_page = LoginEnUSPage(driver)
        home_page = HomeEnUSPage(driver)
        landing_page = LandingEnUSPage(driver)
        
        # Go directly to the Login page (skips Landing page because it is not being tested in these tests)
        login_page.load()
        
        # Select or unselect 'Rememeber me' according to testdata
        if remember_me:
            # Ensure that 'Remember me' is NOT selected"
            login_page.remember_me()
        else:
            # Ensure that 'Remember me' is NOT selected"
            login_page.dont_remember_me()
        
        # Login with valid credentials to get to the Home page
        login_page.login()
        home_page.wait_for_page_to_load(5)
        
        # Attempt to log out from the Home page
        home_page.logout()
        
        # The expected result of a successful logout is the Landing page (i.e. logged out)
        landing_page.wait_for_page_to_load(5)
        assert landing_page.is_current_page()
        
        # Close the browser and end the session
        DriverManager.quit_session()
        
        # Open and new browser and session
        new_driver = DriverManager.get_driver()
        
        # Set up a new Landing page instance
        new_landing_page = LandingEnUSPage(new_driver)
        new_landing_page.load()
        new_landing_page.wait_for_page_to_load(5)
        
        # The expected result of a new session after logout is the Landing page (i.e. still logged out)
        assert new_landing_page.is_current_page()
    
    @pytest.mark.parametrize("test_case, remember_me", remember_me_testdata)
    def test_close_window_keep_session_without_and_with_remember_me(self, driver, test_case, remember_me):
        
        """
        Test that verifies that closing all of the Hudl site windows but keeping a 
        browser session active (i.e. at least one other window is open) does not result 
        in an unexpected logout without or with 'Remember me' was on login.
        
        TODO - determine if it is desirable and feasible to log the user out when the 
        last window for Hudl is closed and 'Remeber me' was NOT selected on login.
        """
        # Set up the Login page, Home page and Landing page instances
        login_page = LoginEnUSPage(driver)
        home_page = HomeEnUSPage(driver)
        landing_page = LandingEnUSPage(driver)
        
        # Go directly to the Login page (skips Landing page because it is not being tested in these tests)
        login_page.load()
        
        # Select or unselect 'Rememeber me' according to testdata
        if remember_me:
            # Ensure that 'Remember me' is NOT selected"
            login_page.remember_me()
        else:
            # Ensure that 'Remember me' is NOT selected"
            login_page.dont_remember_me()
        
        # Login with valid credentials to get to the Home page
        login_page.login()
        home_page.wait_for_page_to_load(5)
        
        # Save the current window handle (just in case it is needed) and then open a new window not on a Hudl page
        primary_window = driver.window_handles[0]
        secondary_window = DriverManager.open_window("https://www.google.com/")
        
        # Close the primary window and switch to the secondary window to simulate closing the last Hudl site page 
        # with other browser windows open to maintain the session.
        DriverManager.close_window()
        DriverManager.switch_to_window(secondary_window)
        
        # Go to the main landing page for hudl.com
        # The expected result is the Home page indicating that the user is still logged in.
        landing_page.load()
        home_page.wait_for_page_to_load(5)
        assert home_page.is_current_page()
    
    @pytest.mark.skip(reason="No way to capture 'Remember me' state between browser sessions. Need to understand mechanism for 'Remember me'")
    @pytest.mark.parametrize("test_case, remember_me", remember_me_testdata)
    def test_end_session_without_logout_without_and_with_remember_me(self, driver, test_case, remember_me):
        
        """
        Test that verifies that ending the browser session without logging out:
            1) Results in a logout if 'Rember me' is NOT selected
            2) Does not result in a logout if 'Remember me' is selected 
            
        TODO - Determine implementation of 'Remember me' function in the browsewr and replicate/simulate between 
        WebDriver browser sessions. Current test(s) try to save and restore cookies, but it does not seem to work.
        """
        # Set up the Login page, Home page and Landing page instances
        login_page = LoginEnUSPage(driver)
        home_page = HomeEnUSPage(driver)
        landing_page = LandingEnUSPage(driver)
        
        # Go directly to the Login page (skips Landing page because it is not being tested in these tests)
        login_page.load()
        
        # Select or unselect 'Rememeber me' according to testdata
        if remember_me:
            # Ensure that 'Remember me' is NOT selected"
            login_page.remember_me()
        else:
            # Ensure that 'Remember me' is NOT selected"
            login_page.dont_remember_me()
        
        # Login with valid credentials to get to the Home page
        login_page.login()
        home_page.wait_for_page_to_load(5)
        
        # Save cookies to ensure that 'Remember me' status is not lost
        DriverManager.save_cookies()
        
        # Close the browser and end the session
        DriverManager.quit_session()
        
        # Open a new browser and session
        new_driver = DriverManager.get_driver()
        
        # Set up a new Landing page and Home page instances
        new_landing_page = LandingEnUSPage(new_driver)
        new_home_page = HomeEnUSPage(new_driver)
        
        # Go to the Hudl site
        new_landing_page.load()
        
        # Restore cookies to get back the 'Remember me' status
        DriverManager.restore_cookies()
        
        if remember_me:
            # The expected result of a new session after logout when 'Remember me' is selected
            # is the Landing page (i.e. still logged in)
            new_home_page.wait_for_page_to_load(5)
            assert new_home_page.is_current_page()
        else:
            # The expected result of a new session after logout when 'Remember me' is NOT selected
            # is the Landing page (i.e. logged out)
            new_landing_page.wait_for_page_to_load(5)
            assert new_landing_page.is_current_page()