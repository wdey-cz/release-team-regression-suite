"""
Registries Page Object Model.
Contains locators and methods for the Registries page.
"""

from selenium.webdriver.common.by import By
from core.base_page import BasePage


class RegistriesPage(BasePage):
    """Page Object Model for the Registries page."""
    
    # Locators
    PAGE_TITLE = (By.CSS_SELECTOR, "h1.page-title")
    REGISTRIES_TABLE = (By.ID, "registries-table")
    ADD_REGISTRY_BUTTON = (By.ID, "add-registry-btn")
    SEARCH_INPUT = (By.ID, "registry-search")
    SEARCH_BUTTON = (By.ID, "search-btn")
    FILTER_DROPDOWN = (By.ID, "registry-filter")
    REGISTRY_ROWS = (By.CSS_SELECTOR, ".registry-row")
    REGISTRY_NAME = (By.CSS_SELECTOR, ".registry-name")
    REGISTRY_STATUS = (By.CSS_SELECTOR, ".registry-status")
    EDIT_REGISTRY_BUTTON = (By.CSS_SELECTOR, ".edit-registry")
    DELETE_REGISTRY_BUTTON = (By.CSS_SELECTOR, ".delete-registry")
    VIEW_DETAILS_BUTTON = (By.CSS_SELECTOR, ".view-details")
    PAGINATION_NEXT = (By.ID, "pagination-next")
    PAGINATION_PREVIOUS = (By.ID, "pagination-prev")
    LOADING_SPINNER = (By.CLASS_NAME, "loading-spinner")
    
    def __init__(self, driver):
        """
        Initialize the Registries page.
        
        Args:
            driver: WebDriver instance
        """
        super().__init__(driver)
    
    def get_page_title_text(self):
        """
        Get the page title text.
        
        Returns:
            Page title text
        """
        return self.get_text(self.PAGE_TITLE)
    
    def is_registries_table_displayed(self):
        """
        Check if the registries table is displayed.
        
        Returns:
            True if table is visible, False otherwise
        """
        return self.is_element_visible(self.REGISTRIES_TABLE)
    
    def click_add_registry(self):
        """Click the Add Registry button."""
        self.click_element(self.ADD_REGISTRY_BUTTON)
    
    def search_registry(self, search_text):
        """
        Search for a registry.
        
        Args:
            search_text: Text to search for
        """
        self.enter_text(self.SEARCH_INPUT, search_text)
        self.click_element(self.SEARCH_BUTTON)
        self.wait_for_loading_complete()
    
    def wait_for_loading_complete(self, timeout=10):
        """
        Wait for loading spinner to disappear.
        
        Args:
            timeout: Maximum time to wait in seconds
        """
        if self.is_element_present(self.LOADING_SPINNER):
            self.wait_helpers.wait_for_element_invisible(self.LOADING_SPINNER, timeout)
    
    def get_registry_count(self):
        """
        Get the total number of registries displayed.
        
        Returns:
            Number of registry rows
        """
        registries = self.find_elements(self.REGISTRY_ROWS)
        return len(registries)
    
    def get_all_registry_names(self):
        """
        Get all registry names from the current page.
        
        Returns:
            List of registry names
        """
        registry_name_elements = self.find_elements(self.REGISTRY_NAME)
        return [element.text for element in registry_name_elements]
    
    def get_registry_status(self, registry_index=0):
        """
        Get the status of a specific registry.
        
        Args:
            registry_index: Index of the registry (0-based)
            
        Returns:
            Status text of the registry
        """
        status_elements = self.find_elements(self.REGISTRY_STATUS)
        if registry_index < len(status_elements):
            return status_elements[registry_index].text
        return None
    
    def click_edit_registry(self, registry_index=0):
        """
        Click the edit button for a specific registry.
        
        Args:
            registry_index: Index of the registry (0-based)
        """
        edit_buttons = self.find_elements(self.EDIT_REGISTRY_BUTTON)
        if registry_index < len(edit_buttons):
            edit_buttons[registry_index].click()
    
    def click_delete_registry(self, registry_index=0):
        """
        Click the delete button for a specific registry.
        
        Args:
            registry_index: Index of the registry (0-based)
        """
        delete_buttons = self.find_elements(self.DELETE_REGISTRY_BUTTON)
        if registry_index < len(delete_buttons):
            delete_buttons[registry_index].click()
    
    def click_view_details(self, registry_index=0):
        """
        Click the view details button for a specific registry.
        
        Args:
            registry_index: Index of the registry (0-based)
        """
        view_buttons = self.find_elements(self.VIEW_DETAILS_BUTTON)
        if registry_index < len(view_buttons):
            view_buttons[registry_index].click()
    
    def go_to_next_page(self):
        """Navigate to the next page of registries."""
        if self.is_element_visible(self.PAGINATION_NEXT, timeout=5):
            self.click_element(self.PAGINATION_NEXT)
            self.wait_for_loading_complete()
    
    def go_to_previous_page(self):
        """Navigate to the previous page of registries."""
        if self.is_element_visible(self.PAGINATION_PREVIOUS, timeout=5):
            self.click_element(self.PAGINATION_PREVIOUS)
            self.wait_for_loading_complete()
    
    def select_filter(self, filter_value):
        """
        Select a filter from the filter dropdown.
        
        Args:
            filter_value: Value to select from the dropdown
        """
        from selenium.webdriver.support.ui import Select
        dropdown_element = self.find_element(self.FILTER_DROPDOWN)
        select = Select(dropdown_element)
        select.select_by_visible_text(filter_value)
        self.wait_for_loading_complete()
