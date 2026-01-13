#!/usr/bin/env python3
"""
Example script demonstrating how to use the page objects directly.
This can be useful for quick testing or debugging.
"""

from core.driver_factory import WebDriverFactory
from core.config import Config
from pages.login_page import LoginPage
from pages.registries_page import RegistriesPage
from pages.patient_dashboard_page import PatientDashboardPage


def main():
    """Main function to demonstrate page object usage."""
    
    # Create WebDriver instance
    print("Initializing WebDriver...")
    driver = WebDriverFactory.get_driver(
        browser_name=Config.get_browser(),
        headless=Config.is_headless()
    )
    
    try:
        # Set timeouts
        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
        
        # Example 1: Login Page
        print("\n=== Testing Login Page ===")
        login_page = LoginPage(driver)
        login_page.navigate_to(f"{Config.get_base_url()}/login")
        
        if login_page.is_login_form_displayed():
            print("✓ Login form is displayed")
        
        # Example 2: Registries Page
        print("\n=== Testing Registries Page ===")
        registries_page = RegistriesPage(driver)
        registries_page.navigate_to(f"{Config.get_base_url()}/registries")
        
        # Uncomment when testing with actual site
        # if registries_page.is_registries_table_displayed():
        #     print("✓ Registries table is displayed")
        #     print(f"  Found {registries_page.get_registry_count()} registries")
        
        # Example 3: Patient Dashboard
        print("\n=== Testing Patient Dashboard ===")
        dashboard_page = PatientDashboardPage(driver)
        dashboard_page.navigate_to(f"{Config.get_base_url()}/patient/dashboard")
        
        # Uncomment when testing with actual site
        # if dashboard_page.is_patient_info_displayed():
        #     print("✓ Patient dashboard is displayed")
        #     patient_name = dashboard_page.get_patient_name()
        #     if patient_name:
        #         print(f"  Patient: {patient_name}")
        
        print("\n=== Test Complete ===")
        
    except Exception as e:
        print(f"\n✗ Error occurred: {str(e)}")
        
    finally:
        # Clean up
        print("\nClosing browser...")
        driver.quit()


if __name__ == "__main__":
    main()
