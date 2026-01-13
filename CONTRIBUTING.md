# Contributing Guide

Thank you for considering contributing to the Release Team Regression Suite! This guide will help you understand how to add new tests and page objects to the framework.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Project Standards](#project-standards)
3. [Adding a New Page Object](#adding-a-new-page-object)
4. [Writing Tests](#writing-tests)
5. [Best Practices](#best-practices)
6. [Code Review Checklist](#code-review-checklist)

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature: `git checkout -b feature/your-feature-name`
4. Install dependencies: `pip install -r requirements.txt`
5. Set up your `.env` file: `cp .env.example .env`

## Project Standards

### Code Style

- Follow PEP 8 Python style guide
- Use meaningful variable and method names
- Add docstrings to all classes and methods
- Keep methods focused and single-purpose
- Maximum line length: 100 characters

### Naming Conventions

- **Files**: Use snake_case (e.g., `patient_dashboard_page.py`)
- **Classes**: Use PascalCase (e.g., `PatientDashboardPage`)
- **Methods**: Use snake_case (e.g., `get_patient_name()`)
- **Constants**: Use UPPER_CASE (e.g., `DEFAULT_TIMEOUT`)
- **Locators**: Use UPPER_CASE (e.g., `LOGIN_BUTTON`)

### Test Organization

- Group related tests in classes
- Use descriptive test names that explain what is being tested
- Add appropriate pytest markers
- One assertion per test when possible

## Adding a New Page Object

### Step 1: Create the Page Object File

Create a new file in the `pages/` directory:

```bash
touch pages/new_feature_page.py
```

### Step 2: Define the Page Object Class

```python
"""
New Feature Page Object Model.
Contains locators and methods for the New Feature page.
"""

from selenium.webdriver.common.by import By
from core.base_page import BasePage


class NewFeaturePage(BasePage):
    """Page Object Model for the New Feature page."""
    
    # Locators - Define all element locators as class constants
    PAGE_TITLE = (By.CSS_SELECTOR, "h1.page-title")
    SUBMIT_BUTTON = (By.ID, "submit-btn")
    INPUT_FIELD = (By.NAME, "input-field")
    RESULT_MESSAGE = (By.CLASS_NAME, "result-message")
    
    def __init__(self, driver):
        """
        Initialize the New Feature page.
        
        Args:
            driver: WebDriver instance
        """
        super().__init__(driver)
    
    def get_page_title_text(self):
        """
        Get the page title text.
        
        Returns:
            Page title text as string
        """
        return self.get_text(self.PAGE_TITLE)
    
    def enter_input(self, text):
        """
        Enter text in the input field.
        
        Args:
            text: Text to enter
        """
        self.enter_text(self.INPUT_FIELD, text)
    
    def click_submit(self):
        """Click the submit button."""
        self.click_element(self.SUBMIT_BUTTON)
    
    def get_result_message(self):
        """
        Get the result message.
        
        Returns:
            Result message text if visible, None otherwise
        """
        if self.is_element_visible(self.RESULT_MESSAGE, timeout=5):
            return self.get_text(self.RESULT_MESSAGE)
        return None
    
    def submit_form(self, input_text):
        """
        Complete form submission workflow.
        
        Args:
            input_text: Text to submit
        """
        self.enter_input(input_text)
        self.click_submit()
```

### Step 3: Update the Pages Package

Add import to `pages/__init__.py` (optional but recommended):

```python
from .new_feature_page import NewFeaturePage
```

## Writing Tests

### Step 1: Create Test File

Create a new file in the `tests/` directory:

```bash
touch tests/test_new_feature.py
```

### Step 2: Write Test Cases

```python
"""
Test cases for New Feature functionality.
"""

import pytest
from pages.new_feature_page import NewFeaturePage


@pytest.mark.regression
class TestNewFeature:
    """Test suite for New Feature page."""
    
    def test_page_loads_successfully(self, driver, base_url):
        """
        Test that the New Feature page loads successfully.
        
        Args:
            driver: WebDriver instance from fixture
            base_url: Base URL from fixture
        """
        page = NewFeaturePage(driver)
        page.navigate_to(f"{base_url}/new-feature")
        
        assert page.is_element_visible(page.PAGE_TITLE)
        assert "New Feature" in page.get_page_title_text()
    
    @pytest.mark.smoke
    def test_form_submission(self, driver, base_url):
        """
        Test form submission functionality.
        
        Args:
            driver: WebDriver instance from fixture
            base_url: Base URL from fixture
        """
        page = NewFeaturePage(driver)
        page.navigate_to(f"{base_url}/new-feature")
        
        test_input = "test data"
        page.submit_form(test_input)
        
        result = page.get_result_message()
        assert result is not None
        assert "success" in result.lower()
    
    def test_empty_form_validation(self, driver, base_url):
        """
        Test that empty form shows validation error.
        
        Args:
            driver: WebDriver instance from fixture
            base_url: Base URL from fixture
        """
        page = NewFeaturePage(driver)
        page.navigate_to(f"{base_url}/new-feature")
        
        page.click_submit()  # Submit without entering data
        
        # Add validation check
        # error_msg = page.get_error_message()
        # assert error_msg is not None
```

## Best Practices

### Page Object Best Practices

1. **Single Responsibility**: Each page object should represent one page
2. **No Assertions**: Page objects should not contain assertions
3. **Return Values**: Methods should return data for tests to assert on
4. **Encapsulation**: Keep locators private to the page object
5. **Reusability**: Create methods for common workflows
6. **Wait Strategies**: Always use explicit waits

### Test Best Practices

1. **Independence**: Tests should not depend on each other
2. **Clean State**: Each test should start with a clean state
3. **Clear Names**: Test names should describe what is being tested
4. **One Concept**: Test one thing at a time
5. **Arrange-Act-Assert**: Follow the AAA pattern
6. **Use Fixtures**: Leverage pytest fixtures for setup/teardown

### Example: Good vs Bad

**Bad:**
```python
# Page Object
def click_login(self):
    self.click_element(self.LOGIN_BUTTON)
    assert self.is_element_visible(self.DASHBOARD)  # ❌ No assertions in page objects

# Test
def test_login(driver):  # ❌ Missing base_url fixture
    driver.get("http://example.com/login")  # ❌ Hardcoded URL
    driver.find_element(By.ID, "username").send_keys("user")  # ❌ Not using page object
```

**Good:**
```python
# Page Object
def click_login(self):
    self.click_element(self.LOGIN_BUTTON)

def is_dashboard_visible(self):
    return self.is_element_visible(self.DASHBOARD)

# Test
def test_login(driver, base_url):  # ✅ Uses fixtures
    login_page = LoginPage(driver)  # ✅ Uses page object
    login_page.navigate_to(f"{base_url}/login")  # ✅ Uses base_url
    login_page.login("user", "pass")
    assert login_page.is_dashboard_visible()  # ✅ Assertion in test
```

## Code Review Checklist

Before submitting a pull request, ensure:

- [ ] All new code has docstrings
- [ ] No hardcoded URLs or credentials
- [ ] Tests use appropriate pytest markers
- [ ] Page objects don't contain assertions
- [ ] Tests are independent and can run in any order
- [ ] All tests pass locally
- [ ] Code follows PEP 8 style guide
- [ ] Locators are descriptive and use appropriate strategies
- [ ] Wait conditions are properly implemented
- [ ] No browser sleep() statements (use explicit waits)
- [ ] README updated if adding new features

## Questions?

If you have questions, please:
1. Check existing documentation
2. Look at similar examples in the codebase
3. Open an issue for discussion

Thank you for contributing! 🎉
