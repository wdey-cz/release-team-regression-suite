"""
Base Page class that all page objects will inherit from.
Contains common functionality and utilities used across all pages.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from core.wait_helpers import WaitHelpers


class BasePage:
    """Base class for all page objects."""
    
    def __init__(self, driver):
        """
        Initialize the base page.
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait_helpers = WaitHelpers(driver)
    
    def find_element(self, locator, timeout=10):
        """
        Find an element with explicit wait.
        
        Args:
            locator: Tuple of (By, locator_value)
            timeout: Maximum time to wait in seconds
            
        Returns:
            WebElement if found
            
        Raises:
            TimeoutException: If element not found within timeout
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def find_elements(self, locator, timeout=10):
        """
        Find multiple elements with explicit wait.
        
        Args:
            locator: Tuple of (By, locator_value)
            timeout: Maximum time to wait in seconds
            
        Returns:
            List of WebElements
        """
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return self.driver.find_elements(*locator)
    
    def click_element(self, locator, timeout=10):
        """
        Click an element after waiting for it to be clickable.
        
        Args:
            locator: Tuple of (By, locator_value)
            timeout: Maximum time to wait in seconds
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
    
    def enter_text(self, locator, text, timeout=10):
        """
        Enter text into an input field after clearing it.
        
        Args:
            locator: Tuple of (By, locator_value)
            text: Text to enter
            timeout: Maximum time to wait in seconds
        """
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator, timeout=10):
        """
        Get text from an element.
        
        Args:
            locator: Tuple of (By, locator_value)
            timeout: Maximum time to wait in seconds
            
        Returns:
            Text content of the element
        """
        element = self.find_element(locator, timeout)
        return element.text
    
    def is_element_visible(self, locator, timeout=10):
        """
        Check if an element is visible.
        
        Args:
            locator: Tuple of (By, locator_value)
            timeout: Maximum time to wait in seconds
            
        Returns:
            True if element is visible, False otherwise
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def is_element_present(self, locator):
        """
        Check if an element is present in the DOM.
        
        Args:
            locator: Tuple of (By, locator_value)
            
        Returns:
            True if element is present, False otherwise
        """
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
    
    def get_page_title(self):
        """
        Get the current page title.
        
        Returns:
            Page title as string
        """
        return self.driver.title
    
    def get_current_url(self):
        """
        Get the current URL.
        
        Returns:
            Current URL as string
        """
        return self.driver.current_url
    
    def navigate_to(self, url):
        """
        Navigate to a specific URL.
        
        Args:
            url: URL to navigate to
        """
        self.driver.get(url)
    
    def refresh_page(self):
        """Refresh the current page."""
        self.driver.refresh()
    
    def scroll_to_element(self, locator, timeout=10):
        """
        Scroll to an element.
        
        Args:
            locator: Tuple of (By, locator_value)
            timeout: Maximum time to wait in seconds
        """
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def switch_to_frame(self, frame_reference):
        """
        Switch to an iframe.
        
        Args:
            frame_reference: Frame name, id, or WebElement
        """
        self.driver.switch_to.frame(frame_reference)
    
    def switch_to_default_content(self):
        """Switch back to the default content (out of any frames)."""
        self.driver.switch_to.default_content()
    
    def accept_alert(self):
        """Accept/confirm an alert dialog."""
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()
    
    def dismiss_alert(self):
        """Dismiss/cancel an alert dialog."""
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.dismiss()
    
    def get_alert_text(self):
        """
        Get the text from an alert dialog.
        
        Returns:
            Alert text as string
        """
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        return alert.text
