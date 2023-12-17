import time
import csv
from faker import Faker
from utilities.readProperties import ReadConfig
from pageObjects.HomePage.Forgot_info import ForgotInfoAction

class TestForgotInfoFeature:
    application_url = ReadConfig.get_application_url()
    forgot_info_page_url = ReadConfig.get_forgot_info_url()

    def test_verifying_info_page_url(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.forgotInforDriver = ForgotInfoAction(self.driver)
        self.forgotInforDriver.click_on_forgot_info_linkText()
        self.forgotInforDriver.validate_forgot_info_url(self.forgot_info_page_url)
        self.driver.close()

    def test_perform_valid_forgot_info_action(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.forgotInforDriver = ForgotInfoAction(self.driver)
        self.forgotInforDriver.click_on_forgot_info_linkText()
        self.forgotInforDriver.enter_valid_data_in_register_form()
        self.forgotInforDriver.click_find_my_login_nfo_button()
        self.driver.close()


    def test_check_empty_case_error_message(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.forgotInforDriver = ForgotInfoAction(self.driver)
        self.forgotInforDriver.click_on_forgot_info_linkText()
        self.forgotInforDriver.click_find_my_login_nfo_button()
        self.forgotInforDriver.verify_empty_case_error_messages()
        self.driver.close()




