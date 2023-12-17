
from utilities.readProperties import ReadConfig

from pageObjects.HomePage.Login import LogInAction

class TestLoginFeature:

    application_url = ReadConfig.get_application_url()

    def test_check_empty_case_both_username_password_error_message(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.logInDriver = LogInAction(self.driver)
        self.logInDriver.click_log_in_button()
        self.logInDriver.validate_error_message()
        self.driver.close()


    def test_check_empty_case_username_error_message(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.logInDriver = LogInAction(self.driver)
        self.logInDriver.enter_username("Username")
        self.logInDriver.click_log_in_button()
        self.logInDriver.validate_error_message()
        self.driver.close()


    def test_check_empty_case_password_error_message(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.logInDriver = LogInAction(self.driver)
        self.logInDriver.enter_password("password")
        self.logInDriver.click_log_in_button()
        self.logInDriver.validate_error_message()
        self.driver.close()


    def test_check_wrong_username_error_message(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.logInDriver = LogInAction(self.driver)
        self.logInDriver.enter_username("Incorrect")
        self.logInDriver.enter_password("password")
        self.logInDriver.click_log_in_button()
        self.logInDriver.validate_error_message()
        self.driver.close()


    def test_check_wrong_password_error_message(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.logInDriver = LogInAction(self.driver)
        self.logInDriver.enter_username("Correct")
        self.logInDriver.enter_password("password")
        self.logInDriver.click_log_in_button()
        self.logInDriver.validate_error_message()
        self.driver.close()


    def test_perform_valid_login_action(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.logInDriver = LogInAction(self.driver)
        self.logInDriver.enter_valid_data_in_login_form()
        self.logInDriver.click_log_in_button()
        self.driver.close()

