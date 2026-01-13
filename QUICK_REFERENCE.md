# Quick Reference Guide

## Common Commands

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
```

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_login.py

# Run with markers
pytest -m smoke
pytest -m regression

# Run in headless mode
HEADLESS=true pytest

# Run with different browser
BROWSER=firefox pytest

# Run tests in parallel (4 workers)
pytest -n 4

# Generate HTML report
pytest --html=reports/report.html
```

### Test Markers
- `@pytest.mark.smoke` - Quick smoke tests
- `@pytest.mark.regression` - Full regression tests
- `@pytest.mark.login` - Login functionality tests
- `@pytest.mark.dashboard` - Dashboard functionality tests
- `@pytest.mark.registries` - Registries functionality tests

## Page Object Model Pattern

### Creating a New Page Object

1. Create file in `pages/` directory
2. Import `BasePage` and `By`
3. Define locators as class variables
4. Implement page-specific methods

```python
from selenium.webdriver.common.by import By
from core.base_page import BasePage

class MyPage(BasePage):
    # Locators
    BUTTON = (By.ID, "my-button")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_button(self):
        self.click_element(self.BUTTON)
```

### Creating a Test

1. Create file in `tests/` directory with `test_` prefix
2. Import page objects
3. Use pytest fixtures (`driver`, `base_url`, etc.)

```python
import pytest
from pages.my_page import MyPage

@pytest.mark.regression
class TestMyPage:
    def test_button_click(self, driver, base_url):
        page = MyPage(driver)
        page.navigate_to(f"{base_url}/my-page")
        page.click_button()
```

## Base Page Methods

### Element Interaction
- `find_element(locator, timeout=10)`
- `find_elements(locator, timeout=10)`
- `click_element(locator, timeout=10)`
- `enter_text(locator, text, timeout=10)`
- `get_text(locator, timeout=10)`

### Element State
- `is_element_visible(locator, timeout=10)`
- `is_element_present(locator)`

### Navigation
- `navigate_to(url)`
- `refresh_page()`
- `get_current_url()`
- `get_page_title()`

### Advanced
- `scroll_to_element(locator, timeout=10)`
- `switch_to_frame(frame_reference)`
- `switch_to_default_content()`
- `accept_alert()`
- `dismiss_alert()`

## Wait Helpers

Access via `self.wait_helpers` in page objects:

- `wait_for_element_visible(locator, timeout=None)`
- `wait_for_element_invisible(locator, timeout=None)`
- `wait_for_element_clickable(locator, timeout=None)`
- `wait_for_text_in_element(locator, text, timeout=None)`
- `wait_for_url_contains(url_fragment, timeout=None)`
- `wait_for_title_contains(title_fragment, timeout=None)`

## Helper Functions

Import from `core.helpers`:

- `Helpers.take_screenshot(driver, name="screenshot")`
- `Helpers.wait(seconds)`
- `Helpers.generate_unique_email(prefix="test")`
- `Helpers.generate_unique_username(prefix="user")`
- `Helpers.scroll_to_bottom(driver)`
- `Helpers.scroll_to_top(driver)`

## Environment Variables

Set in `.env` file:

| Variable | Default | Options |
|----------|---------|---------|
| BASE_URL | `https://www.cozeva.com` | Any URL |
| BROWSER | `chrome` | `chrome`, `firefox`, `edge` |
| HEADLESS | `false` | `true`, `false` |
| DEFAULT_TIMEOUT | `10` | Seconds |
| PAGE_LOAD_TIMEOUT | `30` | Seconds |
| TEST_USERNAME | - | String |
| TEST_PASSWORD | - | String |

## Directory Structure

```
├── config/          # Configuration package
├── core/            # Core utilities
│   ├── base_page.py
│   ├── config.py
│   ├── driver_factory.py
│   ├── helpers.py
│   └── wait_helpers.py
├── pages/           # Page objects
├── tests/           # Test cases
├── reports/         # Test reports (auto-generated)
├── screenshots/     # Screenshots (auto-generated)
├── conftest.py      # Pytest fixtures
└── pytest.ini       # Pytest config
```

## Tips

1. Always use explicit waits via `wait_helpers` or base page methods
2. Keep page objects focused on page interactions only
3. Keep test logic in test files, not in page objects
4. Use descriptive method and variable names
5. Add docstrings to page object methods
6. Use pytest markers to organize tests
7. Never commit credentials to version control
