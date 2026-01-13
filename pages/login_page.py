"""
Login Page Object Model.
Contains locators and methods for the login page.
"""

from selenium.webdriver.common.by import By
from core.base_page import BasePage


class LoginPage(BasePage):
    """Page Object Model for the Login page."""
    
    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot Password?")
    REMEMBER_ME_CHECKBOX = (By.ID, "remember-me")
    LOGIN_FORM = (By.ID, "login-form")
    
    def __init__(self, driver):
        """
        Initialize the Login page.
        
        Args:
            driver: WebDriver instance
        """
        super().__init__(driver)
    
    def enter_username(self, username):
        """
        Enter username in the username field.
        
        Args:
            username: Username to enter
        """
        self.enter_text(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """
        Enter password in the password field.
        
        Args:
            password: Password to enter
        """
        self.enter_text(self.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """Click the login button."""
        self.click_element(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """
        Perform login with username and password.
        
        Args:
            username: Username to login with
            password: Password to login with
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def is_login_form_displayed(self):
        """
        Check if the login form is displayed.
        
        Returns:
            True if login form is visible, False otherwise
        """
        return self.is_element_visible(self.LOGIN_FORM)
    
    def get_error_message(self):
        """
        Get the error message text.
        
        Returns:
            Error message text if visible, None otherwise
        """
        if self.is_element_visible(self.ERROR_MESSAGE, timeout=5):
            return self.get_text(self.ERROR_MESSAGE)
        return None
    
    def click_forgot_password(self):
        """Click the forgot password link."""
        self.click_element(self.FORGOT_PASSWORD_LINK)
    
    def check_remember_me(self):
        """Check the 'Remember Me' checkbox."""
        if not self.is_element_present(self.REMEMBER_ME_CHECKBOX):
            return
        checkbox = self.find_element(self.REMEMBER_ME_CHECKBOX)
        if not checkbox.is_selected():
            self.click_element(self.REMEMBER_ME_CHECKBOX)
    
    def uncheck_remember_me(self):
        """Uncheck the 'Remember Me' checkbox."""
        if not self.is_element_present(self.REMEMBER_ME_CHECKBOX):
            return
        checkbox = self.find_element(self.REMEMBER_ME_CHECKBOX)
        if checkbox.is_selected():
            self.click_element(self.REMEMBER_ME_CHECKBOX)
    
    def is_remember_me_checked(self):
        """
        Check if 'Remember Me' checkbox is checked.
        
        Returns:
            True if checked, False otherwise
        """
        if not self.is_element_present(self.REMEMBER_ME_CHECKBOX):
            return False
        checkbox = self.find_element(self.REMEMBER_ME_CHECKBOX)
        return checkbox.is_selected()
