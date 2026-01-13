# Release Team Regression Suite

A comprehensive Selenium-based regression test suite for the Cozeva website, built using the Page Object Model (POM) design pattern with Python and Pytest.

## 📋 Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Writing New Tests](#writing-new-tests)
- [Page Objects](#page-objects)
- [Contributing](#contributing)

## 🗂️ Project Structure

```
release-team-regression-suite/
│
├── config/                    # Configuration files
│   └── __init__.py
│
├── core/                      # Core utilities and base classes
│   ├── __init__.py
│   ├── base_page.py          # Base page class with common methods
│   ├── config.py             # Configuration management
│   ├── driver_factory.py     # WebDriver factory for browser setup
│   ├── helpers.py            # Utility helper functions
│   └── wait_helpers.py       # Wait utilities and custom conditions
│
├── pages/                     # Page Object Model classes
│   ├── __init__.py
│   ├── login_page.py         # Login page object
│   ├── registries_page.py    # Registries page object
│   └── patient_dashboard_page.py  # Patient dashboard page object
│
├── tests/                     # Test cases
│   ├── __init__.py
│   ├── test_login.py         # Login tests
│   ├── test_registries.py    # Registries tests
│   └── test_patient_dashboard.py  # Patient dashboard tests
│
├── conftest.py               # Pytest fixtures and configuration
├── pytest.ini                # Pytest configuration
├── requirements.txt          # Python dependencies
├── .env.example             # Example environment variables
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## ✨ Features

- **Page Object Model (POM)**: Clean separation of test code and page-specific code
- **Reusable Components**: Base page class with common web element interactions
- **Flexible WebDriver Management**: Support for Chrome, Firefox, and Edge browsers
- **Wait Utilities**: Comprehensive wait helpers for reliable test execution
- **Configuration Management**: Environment-based configuration using .env files
- **Screenshot on Failure**: Automatic screenshot capture when tests fail
- **Pytest Integration**: Powerful testing framework with fixtures and markers
- **HTML Reports**: Generate detailed HTML test reports
- **Parallel Execution**: Run tests in parallel using pytest-xdist
- **Custom Markers**: Organize tests with custom markers (smoke, regression, etc.)

## 📦 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Chrome/Firefox/Edge browser installed

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/wdey-cz/release-team-regression-suite.git
   cd release-team-regression-suite
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

1. **Create environment configuration:**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` file with your settings:**
   ```ini
   BASE_URL=https://www.cozeva.com
   BROWSER=chrome
   HEADLESS=false
   DEFAULT_TIMEOUT=10
   TEST_USERNAME=your_username
   TEST_PASSWORD=your_password
   ```

### Configuration Options

| Variable | Description | Default | Options |
|----------|-------------|---------|---------|
| `BASE_URL` | Base URL of the application | `https://www.cozeva.com` | Any valid URL |
| `BROWSER` | Browser to use for tests | `chrome` | `chrome`, `firefox`, `edge` |
| `HEADLESS` | Run browser in headless mode | `false` | `true`, `false` |
| `DEFAULT_TIMEOUT` | Default wait timeout (seconds) | `10` | Any positive integer |
| `PAGE_LOAD_TIMEOUT` | Page load timeout (seconds) | `30` | Any positive integer |
| `SCREENSHOT_ON_FAILURE` | Take screenshot on test failure | `true` | `true`, `false` |

## 🧪 Running Tests

### Run All Tests
```bash
pytest
```

### Run Specific Test File
```bash
pytest tests/test_login.py
```

### Run Tests by Marker
```bash
# Run only smoke tests
pytest -m smoke

# Run only regression tests
pytest -m regression

# Run login tests
pytest -m login

# Run dashboard tests
pytest -m dashboard

# Run registries tests
pytest -m registries
```

### Run Tests in Parallel
```bash
pytest -n 4  # Run with 4 workers
```

### Run Tests in Headless Mode
```bash
HEADLESS=true pytest
```

### Run Tests with Different Browser
```bash
BROWSER=firefox pytest
```

### Generate HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

## 📝 Writing New Tests

### 1. Create a New Page Object

Create a new file in the `pages/` directory:

```python
from selenium.webdriver.common.by import By
from core.base_page import BasePage

class NewPage(BasePage):
    # Define locators
    ELEMENT_LOCATOR = (By.ID, "element-id")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def perform_action(self):
        self.click_element(self.ELEMENT_LOCATOR)
```

### 2. Create a Test File

Create a new file in the `tests/` directory:

```python
import pytest
from pages.new_page import NewPage

@pytest.mark.regression
class TestNewPage:
    def test_something(self, driver, base_url):
        page = NewPage(driver)
        page.navigate_to(f"{base_url}/new-page")
        page.perform_action()
        assert page.is_element_visible(page.ELEMENT_LOCATOR)
```

## 📄 Page Objects

### Available Page Objects

1. **LoginPage** (`pages/login_page.py`)
   - Methods: `login()`, `enter_username()`, `enter_password()`, `click_login_button()`, etc.

2. **RegistriesPage** (`pages/registries_page.py`)
   - Methods: `search_registry()`, `click_add_registry()`, `get_registry_count()`, etc.

3. **PatientDashboardPage** (`pages/patient_dashboard_page.py`)
   - Methods: `get_patient_name()`, `click_vitals_tab()`, `get_risk_score()`, etc.

### Base Page Methods

All page objects inherit from `BasePage` with these common methods:

- `find_element(locator, timeout)` - Find a single element
- `find_elements(locator, timeout)` - Find multiple elements
- `click_element(locator, timeout)` - Click an element
- `enter_text(locator, text, timeout)` - Enter text in an input field
- `get_text(locator, timeout)` - Get text from an element
- `is_element_visible(locator, timeout)` - Check if element is visible
- `is_element_present(locator)` - Check if element is in DOM
- `scroll_to_element(locator, timeout)` - Scroll to an element
- And many more...

## 🤝 Contributing

1. Create a new branch for your feature
2. Write tests following the existing pattern
3. Ensure all tests pass
4. Submit a pull request

## 📧 Support

For issues and questions, please open an issue on GitHub.

---

**Note**: This is a test automation framework. Make sure to update the page locators and test assertions based on the actual Cozeva website structure.