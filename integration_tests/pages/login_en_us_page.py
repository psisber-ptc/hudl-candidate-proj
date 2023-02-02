from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from integration_tests import config
from integration_tests import user_creds
from integration_tests.pages.base_page import BasePage

class LoginEnUSPage(BasePage):
    
    """
    Encapsulates and abstracts all details that tests need to interact with the English US Login page
    """
    
    def __init__(self, driver):
        """
        Initializes this specific page object by initializing attribute inherited from the Base page, 
        setting page specific values and defining locators needed to interact with the page.

        Args:
            driver webdriver: Shared webdriver passed in from the test
        """
        # Initialize attributes inherited from the Base page
        super(LoginEnUSPage, self).__init__(driver)
        
        # Customize the URL for this page
        self._url = self._baseurl + "/login/"
        
        # Customize the locator that is used to determine if the page has loaded
        self._page_loaded_indicator = (By.ID, "app")
        
        # Dictionary of locators to be used to interact with the page.
        # Invoked by _content[locator key]. Locator is a tuple (By, selector string). Tuple is unpacked by '*'
        self._content = {
                            "email_field": (By.ID, "email"),
                            "password_field": (By.ID, "password"),
                            "login_button": (By.CSS_SELECTOR, "button"),
                            "remember_me": (By.CSS_SELECTOR, "input[data-qa-id='remember-me-checkbox']"),
                            "remember_me_unchecked": (By.CSS_SELECTOR, "div[class^='uni-form__check-item']:not([class$='is-checked'])"),
                            "remember_me_checked": (By.CSS_SELECTOR, "div[class^='uni-form__check-item'][class$='is-checked']"),
                            "need_help": (By.CSS_SELECTOR, "a[data-qa-id='need-help-link']"),
                            "sign_up": (By.CSS_SELECTOR, "a[class*='signUpLink']"),
                            "login_failed_message": (By.CSS_SELECTOR, "*[data-qa-id='error-display']")
                            }
    
    def login_with_email_and_password(self, email, password):
        """
        Invoked by tests to log in with specified email and password.

        Args:
            email str: value for email field
            password str: value for password field
        """
        self.driver.find_element(*(self._content["email_field"])).send_keys(email)
        self.driver.find_element(*(self._content["password_field"])).send_keys(password)
        self.driver.find_element(*(self._content["login_button"])).click()
    
    def login(self):
        """
        Log in using valid credentials. Convenience method for tests that just need to log in
        """
        self.login_with_email_and_password(user_creds.email, user_creds.password)
    
    
    def need_help(self):
        """
        Invoked by tests to click on the 'Need help?' link
        """
        self.driver.find_element(*(self._content["need_help"])).click()
    
    def remember_me(self):
        """
        Invoked by tests to ensure the 'Remember me' checkbox is checked
        Uses helper method _click_blocked_element() from Base page to get around issues clicking the link
        """
        # If the checkbox is unchecked then check it
        if self.driver.find_element(*(self._content["remember_me_unchecked"])).is_displayed():
            _check_box = self.driver.find_element(*(self._content["remember_me"]))
            self._click_blocked_element(_check_box)
        # If the checkbox is already checked then no action is necessary
        elif self.driver.find_element(*(self._content["remember_me_checked"])).is_displayed():
            return
    
    def dont_remember_me(self):
        """
        Invoked by tests to ensure the 'Remember me' checkbox is unchecked
        Uses helper method _click_blocked_element() from Base page to get around issues clicking the link
        """
        # If the checkbox is already unchecked then no action is necessary
        if self.driver.find_element(*(self._content["remember_me_unchecked"])).is_displayed():
            return
        # If the checkbox is checked then uncheck it
        elif self.driver.find_element(*(self._content["remember_me_checked"])):
            _check_box = self.driver.find_element(*(self._content["remember_me"]))
            self._click_blocked_element(_check_box)
    
    def sign_up(self):
        """
        Invoked by tests to click on the 'Sign up' link
        """
        self.driver.find_element(*(self._content["sign_up"])).click()
    
    def login_failed(self):
        """
        Invoked by tests to determine whether or not the login failed.
        Uses _is_displayed() in Base page
        Returns:
            bool: True=Failed False = succeeded
        """
        # If the login failed message is displayed within the timeout then return True
        # Otherwise False
        # Logic and try/except are implemented in _is_displayed() in Base page
        return self._is_displayed(self._content["login_failed_message"], 2)
    
    
    