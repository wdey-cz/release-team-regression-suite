"""
WebDriver manager for creating and configuring WebDriver instances.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class WebDriverFactory:
    """Factory class for creating WebDriver instances."""
    
    @staticmethod
    def get_driver(browser_name="chrome", headless=False, **kwargs):
        """
        Create and return a WebDriver instance.
        
        Args:
            browser_name: Name of the browser (chrome, firefox, edge)
            headless: Run browser in headless mode
            **kwargs: Additional arguments for browser options
            
        Returns:
            WebDriver instance
            
        Raises:
            ValueError: If browser_name is not supported
        """
        browser_name = browser_name.lower()
        
        if browser_name == "chrome":
            return WebDriverFactory._get_chrome_driver(headless, **kwargs)
        elif browser_name == "firefox":
            return WebDriverFactory._get_firefox_driver(headless, **kwargs)
        elif browser_name == "edge":
            return WebDriverFactory._get_edge_driver(headless, **kwargs)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
    
    @staticmethod
    def _get_chrome_driver(headless=False, **kwargs):
        """
        Create Chrome WebDriver instance.
        
        Args:
            headless: Run browser in headless mode
            **kwargs: Additional Chrome options
            
        Returns:
            Chrome WebDriver instance
        """
        options = ChromeOptions()
        
        if headless:
            options.add_argument("--headless")
        
        # Common Chrome arguments
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        
        # Add custom arguments if provided
        if "arguments" in kwargs:
            for arg in kwargs["arguments"]:
                options.add_argument(arg)
        
        # Add experimental options if provided
        if "experimental_options" in kwargs:
            for key, value in kwargs["experimental_options"].items():
                options.add_experimental_option(key, value)
        
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        
        return driver
    
    @staticmethod
    def _get_firefox_driver(headless=False, **kwargs):
        """
        Create Firefox WebDriver instance.
        
        Args:
            headless: Run browser in headless mode
            **kwargs: Additional Firefox options
            
        Returns:
            Firefox WebDriver instance
        """
        options = FirefoxOptions()
        
        if headless:
            options.add_argument("--headless")
        
        # Add custom arguments if provided
        if "arguments" in kwargs:
            for arg in kwargs["arguments"]:
                options.add_argument(arg)
        
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        driver.maximize_window()
        
        return driver
    
    @staticmethod
    def _get_edge_driver(headless=False, **kwargs):
        """
        Create Edge WebDriver instance.
        
        Args:
            headless: Run browser in headless mode
            **kwargs: Additional Edge options
            
        Returns:
            Edge WebDriver instance
        """
        options = EdgeOptions()
        
        if headless:
            options.add_argument("--headless")
        
        # Common Edge arguments
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        
        # Add custom arguments if provided
        if "arguments" in kwargs:
            for arg in kwargs["arguments"]:
                options.add_argument(arg)
        
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)
        driver.maximize_window()
        
        return driver
