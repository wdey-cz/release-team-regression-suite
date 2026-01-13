"""
Pytest configuration file (conftest.py).
Contains fixtures and hooks for the test suite.
"""

import pytest
from core.driver_factory import WebDriverFactory
from core.config import Config
from core.helpers import Helpers


@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture to initialize and quit WebDriver for each test.
    
    Args:
        request: Pytest request object
        
    Yields:
        WebDriver instance
    """
    # Setup: Create WebDriver
    browser = Config.get_browser()
    headless = Config.is_headless()
    driver = WebDriverFactory.get_driver(browser_name=browser, headless=headless)
    
    # Set timeouts
    driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
    if Config.IMPLICIT_WAIT > 0:
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
    
    # Yield driver to the test
    yield driver
    
    # Teardown: Take screenshot on failure and quit driver
    if request.node.rep_call.failed and Config.SCREENSHOT_ON_FAILURE:
        test_name = request.node.name
        Helpers.take_screenshot(driver, f"failed_{test_name}")
    
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """
    Session-level fixture to set up the test environment.
    Runs once before all tests.
    """
    # Create necessary directories
    Config.setup_directories()
    print("\n=== Test Environment Setup Complete ===")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to make test results available to fixtures.
    
    This allows fixtures to access test pass/fail status.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


def pytest_configure(config):
    """
    Configure pytest with custom markers and settings.
    
    Args:
        config: Pytest config object
    """
    # Register custom markers
    config.addinivalue_line(
        "markers", "smoke: mark test as a smoke test"
    )
    config.addinivalue_line(
        "markers", "regression: mark test as a regression test"
    )
    config.addinivalue_line(
        "markers", "login: tests related to login functionality"
    )
    config.addinivalue_line(
        "markers", "dashboard: tests related to dashboard functionality"
    )
    config.addinivalue_line(
        "markers", "registries: tests related to registries functionality"
    )


@pytest.fixture
def base_url():
    """
    Fixture to provide the base URL.
    
    Returns:
        Base URL string
    """
    return Config.get_base_url()


@pytest.fixture
def test_credentials():
    """
    Fixture to provide test credentials.
    
    Returns:
        Tuple of (username, password)
    """
    return Config.get_credentials()
