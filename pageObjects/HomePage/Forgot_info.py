import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Methods.methods import Methods
from selenium.webdriver.support import expected_conditions as ec
from faker import Faker
import csv
import pandas as pd

fake = Faker()


class ForgotInfoAction:

    def __init__(self, driver):
        self.driver = driver

    # locators Lists
    forgot_info_xp = "//a[contains(text(),'Forgot login info?')]"

    firstName_input_field_id = "firstName"
    lastName_input_field_id = "lastName"
    address_street_input_field_id  = "address.street"
    address_city_input_field_id  = "address.city"
    address_state_input_field_id  = "address.state"
    address_zipCode_input_field_id = "address.zipCode"
    customer_ssn_input_field_id = "ssn"
    find_my_login_info_button_xp = "//input[@value = 'Find My Login Info']"


    firstName_empty_case_error_message_id = "firstName.errors"
    lastName_empty_case_error_message_id = "lastName.errors"
    address_street_empty_error_message_id = "address.street.errors"
    address_city_empty_error_message_id = "address.city.errors"
    address_state_empty_error_message_id = "address.state.errors"
    address_zipCode_empty_case_error_message_id = "address.zipCode.errors"
    customer_ssn_empty_case_error_message_id = "ssn.errors"

    firstName_empty_case_error_message = "First name is required."
    lastName_empty_case_error_message = "Last name is required."
    address_street_empty_error_message = "Address is required."
    address_city_empty_error_message = "City is required."
    address_state_empty_error_message = "State is required."
    address_zipCode_empty_case_error_message = "Zip Code is required."
    customer_ssn_empty_case_error_message = "Social Security Number is required."



    def click_on_forgot_info_linkText(self):
        Methods(self.driver).click_element(self.forgot_info_xp)

    def validate_forgot_info_url(self,required_url):
        featureName = "Forgot Info"
        received_url = self.driver.current_url
        Methods(self.driver).validate_url(received_url,required_url,featureName)

    def enter_firstName(self,firstname):
        Methods(self.driver).enter_data_id(self.firstName_input_field_id, firstname)


    def enter_lastName(self,lastName):
        Methods(self.driver).enter_data_id(self.lastName_input_field_id,lastName)

    def enter_streetName(self,streetName):
        Methods(self.driver).enter_data_id(self.address_street_input_field_id,streetName)

    def enter_city(self,city):
        Methods(self.driver).enter_data_id(self.address_city_input_field_id,city)

    def enter_state(self,state):
        Methods(self.driver).enter_data_id(self.address_state_input_field_id,state)

    def enter_zipCode(self,zipCode):
        Methods(self.driver).enter_data_id(self.address_zipCode_input_field_id,zipCode)

    def enter_ssn(self,customer_ssn):
        Methods(self.driver).enter_data_id(self.customer_ssn_input_field_id,customer_ssn)

    def click_find_my_login_nfo_button(self):
        Methods(self.driver).click_element(self.find_my_login_info_button_xp)

    def read_data_from_csv_file(self):


        # Read the CSV file
        data = pd.read_csv('profile_data.csv')

        # Access and manipulate the data as needed
        # For example, let's print the first few rows of the data
        print(data.head())

        # Convert data to an array
        data_array = data.values

        # Print the array
        print(data_array)
        return data_array

    def verify_empty_case_error_messages(self):

        #verifying first name error message for empty case
        element_name = "first name"
        #Getting error messages
        error_message = Methods(self.driver).get_error_messages(self.firstName_empty_case_error_message_id)
        Methods(self.driver).assertion_check(error_message, self.firstName_empty_case_error_message, element_name)

        #verifying last name error message for empty case
        element_name = "last name"
        error_message = Methods(self.driver).get_error_messages(self.lastName_empty_case_error_message_id)
        Methods(self.driver).assertion_check(error_message, self.lastName_empty_case_error_message, element_name)

        #verifying street name error message for empty case
        element_name = "street name"
        error_message = Methods(self.driver).get_error_messages(self.address_street_empty_error_message_id)
        Methods(self.driver).assertion_check(error_message, self.address_street_empty_error_message, element_name)

        #verifying city name error message for empty case
        element_name = " city name"
        error_message = Methods(self.driver).get_error_messages(self.address_city_empty_error_message_id)
        Methods(self.driver).assertion_check(error_message, self.address_city_empty_error_message, element_name)



        #verifying state name error message for empty case
        element_name = "state name"
        error_message = Methods(self.driver).get_error_messages(self.address_state_empty_error_message_id)
        Methods(self.driver).assertion_check(error_message, self.address_state_empty_error_message, element_name)


        #verifying Zip Code error message for empty case
        element_name = "Zip code"
        error_message = Methods(self.driver).get_error_messages(self.address_zipCode_empty_case_error_message_id)
        Methods(self.driver).assertion_check(error_message, self.address_zipCode_empty_case_error_message, element_name)


        #verifying security number error message for empty case
        element_name  = " security number"
        error_message = Methods(self.driver).get_error_messages(self.customer_ssn_empty_case_error_message_id)
        Methods(self.driver).assertion_check(error_message, self.customer_ssn_empty_case_error_message, element_name)


    def enter_valid_data_in_register_form(self):

        #Reading the csv file
        data = pd.read_csv('profile_data.csv')

        print(data.head())

        username = data.iloc[1, 0]
        password = data.iloc[1, 0]

        first_name = data.iloc[0, 2]
        last_name = data.iloc[0, 3]
        street_name = data.iloc[0, 4]
        city_name = data.iloc[0, 5]
        state_name = data.iloc[0, 6]
        zip_code1 = data.iloc[0, 8]
        zip_code = str(zip_code1)
        ssn = data.iloc[0, 7]
        user_name = data.iloc[0, 0]
        password = data.iloc[0, 1]


        print(first_name, last_name,ssn,street_name,city_name,zip_code,user_name,password)

        # Entering valid data in first name field
        Methods(self.driver).enter_data_id(self.firstName_input_field_id,first_name)
        time.sleep(2)

        # Entering valid data in last name field
        Methods(self.driver).enter_data_id(self.lastName_input_field_id, last_name)
        time.sleep(2)

        # Entering valid data in Address field
        Methods(self.driver).enter_data_id(self.address_street_input_field_id, street_name)
        time.sleep(2)

        # Entering valid data in City field
        Methods(self.driver).enter_data_id(self.address_city_input_field_id, city_name)
        time.sleep(2)

        # Entering valid data in state field
        Methods(self.driver).enter_data_id(self.address_state_input_field_id, state_name)
        time.sleep(2)

        # Entering valid data in Zip Code
        Methods(self.driver).enter_data_id(self.address_zipCode_input_field_id, zip_code)
        time.sleep(2)

        # Entering valid data in ssn
        Methods(self.driver).enter_data_id(self.customer_ssn_input_field_id, ssn)
        time.sleep(2)



