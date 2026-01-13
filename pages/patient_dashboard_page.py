"""
Patient Dashboard Page Object Model.
Contains locators and methods for the Patient Dashboard page.
"""

from selenium.webdriver.common.by import By
from core.base_page import BasePage


class PatientDashboardPage(BasePage):
    """Page Object Model for the Patient Dashboard page."""
    
    # Locators
    DASHBOARD_HEADER = (By.CSS_SELECTOR, "h1.dashboard-header")
    PATIENT_NAME = (By.ID, "patient-name")
    PATIENT_ID = (By.ID, "patient-id")
    PATIENT_INFO_SECTION = (By.CLASS_NAME, "patient-info")
    VITALS_SECTION = (By.ID, "vitals-section")
    MEDICATIONS_SECTION = (By.ID, "medications-section")
    APPOINTMENTS_SECTION = (By.ID, "appointments-section")
    MEDICAL_HISTORY_SECTION = (By.ID, "medical-history-section")
    
    # Tabs
    OVERVIEW_TAB = (By.ID, "overview-tab")
    VITALS_TAB = (By.ID, "vitals-tab")
    MEDICATIONS_TAB = (By.ID, "medications-tab")
    APPOINTMENTS_TAB = (By.ID, "appointments-tab")
    DOCUMENTS_TAB = (By.ID, "documents-tab")
    
    # Action buttons
    ADD_VITAL_BUTTON = (By.ID, "add-vital-btn")
    ADD_MEDICATION_BUTTON = (By.ID, "add-medication-btn")
    SCHEDULE_APPOINTMENT_BUTTON = (By.ID, "schedule-appointment-btn")
    UPLOAD_DOCUMENT_BUTTON = (By.ID, "upload-document-btn")
    EDIT_PATIENT_INFO_BUTTON = (By.ID, "edit-patient-info-btn")
    
    # Patient details
    PATIENT_AGE = (By.CLASS_NAME, "patient-age")
    PATIENT_GENDER = (By.CLASS_NAME, "patient-gender")
    PATIENT_DOB = (By.CLASS_NAME, "patient-dob")
    PATIENT_PHONE = (By.CLASS_NAME, "patient-phone")
    PATIENT_EMAIL = (By.CLASS_NAME, "patient-email")
    PATIENT_ADDRESS = (By.CLASS_NAME, "patient-address")
    
    # Lists and tables
    VITALS_LIST = (By.CSS_SELECTOR, ".vital-item")
    MEDICATIONS_LIST = (By.CSS_SELECTOR, ".medication-item")
    APPOINTMENTS_LIST = (By.CSS_SELECTOR, ".appointment-item")
    
    # Status indicators
    RISK_SCORE = (By.ID, "risk-score")
    RISK_LEVEL = (By.CLASS_NAME, "risk-level")
    ALERT_BANNER = (By.CLASS_NAME, "alert-banner")
    
    def __init__(self, driver):
        """
        Initialize the Patient Dashboard page.
        
        Args:
            driver: WebDriver instance
        """
        super().__init__(driver)
    
    def get_dashboard_header_text(self):
        """
        Get the dashboard header text.
        
        Returns:
            Dashboard header text
        """
        return self.get_text(self.DASHBOARD_HEADER)
    
    def get_patient_name(self):
        """
        Get the patient name.
        
        Returns:
            Patient name text
        """
        return self.get_text(self.PATIENT_NAME)
    
    def get_patient_id(self):
        """
        Get the patient ID.
        
        Returns:
            Patient ID text
        """
        return self.get_text(self.PATIENT_ID)
    
    def is_patient_info_displayed(self):
        """
        Check if patient info section is displayed.
        
        Returns:
            True if patient info is visible, False otherwise
        """
        return self.is_element_visible(self.PATIENT_INFO_SECTION)
    
    # Tab navigation methods
    def click_overview_tab(self):
        """Click the Overview tab."""
        self.click_element(self.OVERVIEW_TAB)
    
    def click_vitals_tab(self):
        """Click the Vitals tab."""
        self.click_element(self.VITALS_TAB)
    
    def click_medications_tab(self):
        """Click the Medications tab."""
        self.click_element(self.MEDICATIONS_TAB)
    
    def click_appointments_tab(self):
        """Click the Appointments tab."""
        self.click_element(self.APPOINTMENTS_TAB)
    
    def click_documents_tab(self):
        """Click the Documents tab."""
        self.click_element(self.DOCUMENTS_TAB)
    
    # Action button methods
    def click_add_vital(self):
        """Click the Add Vital button."""
        self.click_element(self.ADD_VITAL_BUTTON)
    
    def click_add_medication(self):
        """Click the Add Medication button."""
        self.click_element(self.ADD_MEDICATION_BUTTON)
    
    def click_schedule_appointment(self):
        """Click the Schedule Appointment button."""
        self.click_element(self.SCHEDULE_APPOINTMENT_BUTTON)
    
    def click_upload_document(self):
        """Click the Upload Document button."""
        self.click_element(self.UPLOAD_DOCUMENT_BUTTON)
    
    def click_edit_patient_info(self):
        """Click the Edit Patient Info button."""
        self.click_element(self.EDIT_PATIENT_INFO_BUTTON)
    
    # Patient details methods
    def get_patient_age(self):
        """
        Get the patient's age.
        
        Returns:
            Patient age text
        """
        if self.is_element_visible(self.PATIENT_AGE, timeout=5):
            return self.get_text(self.PATIENT_AGE)
        return None
    
    def get_patient_gender(self):
        """
        Get the patient's gender.
        
        Returns:
            Patient gender text
        """
        if self.is_element_visible(self.PATIENT_GENDER, timeout=5):
            return self.get_text(self.PATIENT_GENDER)
        return None
    
    def get_patient_dob(self):
        """
        Get the patient's date of birth.
        
        Returns:
            Patient DOB text
        """
        if self.is_element_visible(self.PATIENT_DOB, timeout=5):
            return self.get_text(self.PATIENT_DOB)
        return None
    
    def get_patient_contact_info(self):
        """
        Get the patient's contact information.
        
        Returns:
            Dictionary with phone, email, and address
        """
        contact_info = {}
        if self.is_element_visible(self.PATIENT_PHONE, timeout=5):
            contact_info['phone'] = self.get_text(self.PATIENT_PHONE)
        if self.is_element_visible(self.PATIENT_EMAIL, timeout=5):
            contact_info['email'] = self.get_text(self.PATIENT_EMAIL)
        if self.is_element_visible(self.PATIENT_ADDRESS, timeout=5):
            contact_info['address'] = self.get_text(self.PATIENT_ADDRESS)
        return contact_info
    
    # List and count methods
    def get_vitals_count(self):
        """
        Get the number of vitals entries.
        
        Returns:
            Number of vital entries
        """
        if self.is_element_visible(self.VITALS_SECTION, timeout=5):
            vitals = self.find_elements(self.VITALS_LIST)
            return len(vitals)
        return 0
    
    def get_medications_count(self):
        """
        Get the number of medications.
        
        Returns:
            Number of medications
        """
        if self.is_element_visible(self.MEDICATIONS_SECTION, timeout=5):
            medications = self.find_elements(self.MEDICATIONS_LIST)
            return len(medications)
        return 0
    
    def get_appointments_count(self):
        """
        Get the number of appointments.
        
        Returns:
            Number of appointments
        """
        if self.is_element_visible(self.APPOINTMENTS_SECTION, timeout=5):
            appointments = self.find_elements(self.APPOINTMENTS_LIST)
            return len(appointments)
        return 0
    
    # Status methods
    def get_risk_score(self):
        """
        Get the patient's risk score.
        
        Returns:
            Risk score text
        """
        if self.is_element_visible(self.RISK_SCORE, timeout=5):
            return self.get_text(self.RISK_SCORE)
        return None
    
    def get_risk_level(self):
        """
        Get the patient's risk level.
        
        Returns:
            Risk level text
        """
        if self.is_element_visible(self.RISK_LEVEL, timeout=5):
            return self.get_text(self.RISK_LEVEL)
        return None
    
    def is_alert_displayed(self):
        """
        Check if an alert banner is displayed.
        
        Returns:
            True if alert is visible, False otherwise
        """
        return self.is_element_visible(self.ALERT_BANNER, timeout=5)
    
    def get_alert_message(self):
        """
        Get the alert message text.
        
        Returns:
            Alert message text if visible, None otherwise
        """
        if self.is_alert_displayed():
            return self.get_text(self.ALERT_BANNER)
        return None
