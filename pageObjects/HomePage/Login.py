import json
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Methods.methods import Methods
from selenium.webdriver.support import expected_conditions as ec
from faker import Faker
import csv

fake = Faker()


class LogInAction:

    def __init__(self, driver):
        self.driver = driver

    # locators Lists
    username_input_field_xp = "//input[@name = 'username']"
    password_input_field_xp = "//input[@name = 'password']"
    log_in_button_xp = "//input[@value = 'Log In']"

    logout_linkText_xp = "//a[contains(text(),'Log Out')]"

    login_error_message_xpath = "//p[contains(text(),'Please enter a username and password.')]"


    def enter_username(self,username):
        Methods(self.driver).enter_data_xpath(self.username_input_field_xp, username)

    def enter_password(self, password):
        Methods(self.driver).enter_data_xpath(self.username_input_field_xp, password)

    def click_log_in_button(self):
        Methods(self.driver).click_element(self.log_in_button_xp)

    def validate_error_message(self):
        element = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH, self.login_error_message_xpath)))
    def perform_logout_action (self):
        Methods(self.driver).click_element(self.logout_linkText_xp)

    def enter_valid_data_in_login_form(self):

        # Read the CSV file
        data = pd.read_csv('profile_data.csv')

        print(data.head())

        username = data.iloc[0,0]
        password = data.iloc[0,1]

        print("This is username " + username)
        print("This is password " + password)

        # Entering valid data in user name field
        Methods(self.driver).enter_data_xpath(self.username_input_field_xp, username)
        time.sleep(2)

        # Entering valid data in password field
        Methods(self.driver).enter_data_xpath(self.password_input_field_xp, password)
        time.sleep(2)

