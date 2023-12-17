
from faker import Faker
from utilities.readProperties import ReadConfig
from pageObjects.HomePage.Register import RegisterAction


fake = Faker()


class TestRegisterFeature:
    application_url = ReadConfig.get_application_url()
    register_page_url = ReadConfig.get_registration_page_url()

    def test_verifying_register_page_url(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.registerDriver = RegisterAction(self.driver)
        self.registerDriver.click_on_register_linkText()
        self.registerDriver.validate_register_page_url(self.register_page_url)
        self.driver.close()

    def test_perform_valid_registeration(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.registerDriver = RegisterAction(self.driver)
        count = 0

        for i in range(2):
            self.registerDriver.click_on_register_linkText()
            self.registerDriver.enter_valid_data_in_register_form()
            self.registerDriver.click_register_button()
            self.registerDriver.validate_register_action()
            self.registerDriver.perform_logout_action()
            self.registerDriver.save_data_in_csv_file(self.registerDriver.profile_array_list)

        self.driver.close()

    def test_check_empty_case_error_message(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.registerDriver = RegisterAction(self.driver)
        self.registerDriver.click_on_register_linkText()
        self.registerDriver.click_register_button()
        self.registerDriver.verify_empty_case_error_messages()
        self.driver.close()


    def test_check_password_not_matched_case(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.registerDriver = RegisterAction(self.driver)
        self.registerDriver.click_on_register_linkText()
        self.registerDriver.enter_in_valid_data_in_confirm_password_register_form()
        self.registerDriver.click_register_button()
        self.registerDriver.verify_password_mismatch_error_message()
        self.driver.close()



