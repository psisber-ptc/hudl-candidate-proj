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

import user_creds
from pages.login_page import LoginPage
from pages.home_page import HomePage

class TestLogin():
    
    def test_valid_credentials(self, driver):
        
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        login_page.load()
        login_page.login_with_email_and_password(user_creds.email, user_creds.password)
        home_page.wait_for_page_to_load()
        
        assert home_page.is_current_page()
            