"""
Sample test file for login functionality.
"""

import pytest
from pages.login_page import LoginPage


@pytest.mark.login
@pytest.mark.smoke
class TestLogin:
    """Test cases for login functionality."""
    
    def test_login_page_loads(self, driver, base_url):
        """
        Test that the login page loads successfully.
        
        Args:
            driver: WebDriver instance from fixture
            base_url: Base URL from fixture
        """
        login_page = LoginPage(driver)
        login_page.navigate_to(f"{base_url}/login")
        
        assert login_page.is_login_form_displayed(), "Login form should be displayed"
        assert "login" in login_page.get_current_url().lower(), "URL should contain 'login'"
    
    def test_login_with_valid_credentials(self, driver, base_url, test_credentials):
        """
        Test login with valid credentials.
        
        Args:
            driver: WebDriver instance from fixture
            base_url: Base URL from fixture
            test_credentials: Test credentials tuple (username, password)
        """
        username, password = test_credentials
        
        # Skip if credentials not provided
        if not username or not password:
            pytest.skip("Test credentials not configured")
        
        login_page = LoginPage(driver)
        login_page.navigate_to(f"{base_url}/login")
        login_page.login(username, password)
        
        # Add assertion based on expected behavior after successful login
        # This is a placeholder - adjust based on actual application behavior
        # assert "dashboard" in login_page.get_current_url().lower()
    
    def test_login_with_invalid_credentials(self, driver, base_url):
        """
        Test login with invalid credentials.
        
        Args:
            driver: WebDriver instance from fixture
            base_url: Base URL from fixture
        """
        login_page = LoginPage(driver)
        login_page.navigate_to(f"{base_url}/login")
        login_page.login("invalid_user", "invalid_password")
        
        # Check for error message
        error_message = login_page.get_error_message()
        # This assertion may need adjustment based on actual error message
        # assert error_message is not None, "Error message should be displayed"
    
    @pytest.mark.regression
    def test_remember_me_checkbox(self, driver, base_url):
        """
        Test the Remember Me checkbox functionality.
        
        Args:
            driver: WebDriver instance from fixture
            base_url: Base URL from fixture
        """
        login_page = LoginPage(driver)
        login_page.navigate_to(f"{base_url}/login")
        
        # Test checking the checkbox
        login_page.check_remember_me()
        # assert login_page.is_remember_me_checked(), "Remember me should be checked"
        
        # Test unchecking the checkbox
        login_page.uncheck_remember_me()
        # assert not login_page.is_remember_me_checked(), "Remember me should be unchecked"
    
    @pytest.mark.regression
    def test_forgot_password_link(self, driver, base_url):
        """
        Test the Forgot Password link.
        
        Args:
            driver: WebDriver instance from fixture
            base_url: Base URL from fixture
        """
        login_page = LoginPage(driver)
        login_page.navigate_to(f"{base_url}/login")
        
        # Click forgot password link
        # login_page.click_forgot_password()
        
        # Add assertion for redirect or modal appearance
        # This depends on actual application behavior
