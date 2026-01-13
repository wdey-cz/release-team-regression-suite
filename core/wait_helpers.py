"""
Wait helper utilities for explicit waits and custom wait conditions.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class WaitHelpers:
    """Helper class for various wait operations."""
    
    def __init__(self, driver, default_timeout=10):
        """
        Initialize wait helpers.
        
        Args:
            driver: WebDriver instance
            default_timeout: Default timeout in seconds
        """
        self.driver = driver
        self.default_timeout = default_timeout
    
    def wait_for_element_visible(self, locator, timeout=None):
        """
        Wait for an element to be visible.
        
        Args:
            locator: Tuple of (By, locator_value)
            timeout: Maximum time to wait in seconds
            
        Returns:
            WebElement if visible within timeout
            
        Raises:
            TimeoutException: If element not visible within timeout
        """
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def wait_for_element_invisible(self, locator, timeout=None):
        """
        Wait for an element to become invisible.
        
        Args:
            locator: Tuple of (By, locator_value)
            timeout: Maximum time to wait in seconds
            
        Returns:
            True if element becomes invisible within timeout
            
        Raises:
            TimeoutException: If element still visible after timeout
        """
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
    
    def wait_for_element_clickable(self, locator, timeout=None):
        """
        Wait for an element to be clickable.
        
        Args:
            locator: Tuple of (By, locator_value)
            timeout: Maximum time to wait in seconds
            
        Returns:
            WebElement if clickable within timeout
            
        Raises:
            TimeoutException: If element not clickable within timeout
        """
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    
    def wait_for_element_present(self, locator, timeout=None):
        """
        Wait for an element to be present in the DOM.
        
        Args:
            locator: Tuple of (By, locator_value)
            timeout: Maximum time to wait in seconds
            
        Returns:
            WebElement if present within timeout
            
        Raises:
            TimeoutException: If element not present within timeout
        """
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def wait_for_text_in_element(self, locator, text, timeout=None):
        """
        Wait for specific text to appear in an element.
        
        Args:
            locator: Tuple of (By, locator_value)
            text: Text to wait for
            timeout: Maximum time to wait in seconds
            
        Returns:
            True if text appears within timeout
            
        Raises:
            TimeoutException: If text doesn't appear within timeout
        """
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )
    
    def wait_for_url_contains(self, url_fragment, timeout=None):
        """
        Wait for URL to contain a specific fragment.
        
        Args:
            url_fragment: URL fragment to wait for
            timeout: Maximum time to wait in seconds
            
        Returns:
            True if URL contains fragment within timeout
            
        Raises:
            TimeoutException: If URL doesn't contain fragment within timeout
        """
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_fragment)
        )
    
    def wait_for_url_to_be(self, url, timeout=None):
        """
        Wait for URL to be exactly a specific value.
        
        Args:
            url: Exact URL to wait for
            timeout: Maximum time to wait in seconds
            
        Returns:
            True if URL matches within timeout
            
        Raises:
            TimeoutException: If URL doesn't match within timeout
        """
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url)
        )
    
    def wait_for_title_contains(self, title_fragment, timeout=None):
        """
        Wait for page title to contain a specific fragment.
        
        Args:
            title_fragment: Title fragment to wait for
            timeout: Maximum time to wait in seconds
            
        Returns:
            True if title contains fragment within timeout
            
        Raises:
            TimeoutException: If title doesn't contain fragment within timeout
        """
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.title_contains(title_fragment)
        )
    
    def wait_for_alert_present(self, timeout=None):
        """
        Wait for an alert to be present.
        
        Args:
            timeout: Maximum time to wait in seconds
            
        Returns:
            Alert object if present within timeout
            
        Raises:
            TimeoutException: If alert not present within timeout
        """
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.alert_is_present()
        )
    
    def wait_for_element_selection_state(self, locator, is_selected, timeout=None):
        """
        Wait for an element's selection state to be a specific value.
        
        Args:
            locator: Tuple of (By, locator_value)
            is_selected: Expected selection state (True/False)
            timeout: Maximum time to wait in seconds
            
        Returns:
            True if selection state matches within timeout
            
        Raises:
            TimeoutException: If selection state doesn't match within timeout
        """
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.element_located_selection_state_to_be(locator, is_selected)
        )
    
    def wait_for_number_of_windows(self, num_windows, timeout=None):
        """
        Wait for a specific number of browser windows.
        
        Args:
            num_windows: Expected number of windows
            timeout: Maximum time to wait in seconds
            
        Returns:
            True if number of windows matches within timeout
            
        Raises:
            TimeoutException: If number of windows doesn't match within timeout
        """
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.number_of_windows_to_be(num_windows)
        )
    
    def wait_for_staleness_of(self, element, timeout=None):
        """
        Wait for an element to become stale (removed from DOM).
        
        Args:
            element: WebElement to wait for
            timeout: Maximum time to wait in seconds
            
        Returns:
            True if element becomes stale within timeout
            
        Raises:
            TimeoutException: If element doesn't become stale within timeout
        """
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.staleness_of(element)
        )
