import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Methods.methods import Methods
from selenium.webdriver.support import expected_conditions as ec
from faker import Faker
import csv

fake = Faker()

class RegisterAction:

    def __init__(self, driver):
        self.driver = driver

    # locators Lists
    register_linkText_xp = "//a[contains(text(),'Register')]"
    logout_linkText_xp  = "//a[contains(text(),'Log Out')]"

    firstName_input_field_id = "customer.firstName"
    lastName_input_field_id = "customer.lastName"
    address_street_input_field_id  = "customer.address.street"
    address_city_input_field_id  = "customer.address.city"
    address_state_input_field_id  = "customer.address.state"
    address_zipCode_input_field_id = "customer.address.zipCode"
    address_PhoneNumber_input_field_id = "customer.phoneNumber"
    customer_ssn_input_field_id = "customer.ssn"
    username_input_field_id = "customer.username"
    password_input_field_id = "customer.password"
    confirm_password_input_field_id  = "repeatedPassword"
    register_button_xp = "//input[@value = 'Register']"

    firstName_empty_case_error_message_id = "customer.firstName.errors"
    lastName_empty_case_error_message_id = "customer.lastName.errors"
    address_street_empty_error_message_id = "customer.address.street.errors"
    address_city_empty_error_message_id = "customer.address.city.errors"
    address_state_empty_error_message_id = "customer.address.state.errors"
    address_zipCode_empty_case_error_message_id = "customer.address.zipCode.errors"
    customer_ssn_empty_case_error_message_id = "customer.ssn.errors"
    username_empty_case_error_message_id = "customer.username.errors"
    password_empty_case_error_message_id = "customer.password.errors"
    confirm_password_empty_case_error_message_id = "repeatedPassword.errors"

    firstName_empty_case_error_message = "First name is required."
    lastName_empty_case_error_message = "Last name is required."
    address_street_empty_error_message = "Address is required."
    address_city_empty_error_message = "City is required."
    address_state_empty_error_message = "State is required."
    address_zipCode_empty_case_error_message = "Zip Code is required."
    customer_ssn_empty_case_error_message = "Social Security Number is required."
    username_empty_case_error_message = "Username is required."
    password_empty_case_error_message = "Password is required."
    confirm_password_empty_case_error_message = "Password confirmation is required."

    password_mismatched_error_message = "Passwords did not match."

    password_mismatched_error_message_id = "repeatedPassword.errors"

    registration_confirmation_message_xpath = "//p[contains(text(),'Your account was created successfully. You are now logged in.')]"

    profile_array_list = []

    def click_on_register_linkText(self):
        Methods(self.driver).click_element(self.register_linkText_xp)

    def enter_firstName(self,firstname):
        Methods(self.driver).enter_data_id(self.firstName_input_field_id, firstname)

    def enter_lastName(self,lastName):
        Methods(self.driver).enter_data_id(self.lastName_input_field_id,lastName)

    def enter_streetName(self,streetName):
        Methods(self.driver).enter_data_id(self.address_street_input_field_id,streetName)

    def enter_city(self, city):
        Methods(self.driver).enter_data_id(self.address_city_input_field_id, city)

    def enter_state(self,state):
        Methods(self.driver).enter_data_id(self.address_state_input_field_id,state)

    def enter_zipCode(self,zipCode):
        Methods(self.driver).enter_data_id(self.address_zipCode_input_field_id,zipCode)

    def enter_phoneNumber(self,phoneNumber):
        Methods(self.driver).enter_data_id(self.address_PhoneNumber_input_field_id,phoneNumber)

    def enter_ssn(self,customer_ssn):
        Methods(self.driver).enter_data_id(self.customer_ssn_input_field_id,customer_ssn)

    def enter_username(self,username):
        Methods(self.driver).enter_data_id(self.username_input_field_id,username)

    def enter_password(self,password):
        Methods(self.driver).enter_data_id(self.password_input_field_id,password)

    def confirm_password(self,password):
        Methods(self.driver).enter_data_id(self.confirm_password_input_field_id,password)

    def validate_register_page_url(self,required_url):
        featureName = "Register"
        received_url = self.driver.current_url
        Methods(self.driver).validate_url(received_url,required_url,featureName)

    def clear_and_enter_mismatched_confirm_password(self,password):
        Methods(self.driver).clear_element_data_using_id(self.confirm_password_input_field_id)
        Methods(self.driver).enter_data_id(self.confirm_password_input_field_id,password)


    def verify_password_mismatch_error_message(self):

        # Getting error messages
        error_message = Methods(self.driver).get_error_messages(self.password_mismatched_error_message_id)
        Methods(self.driver).assertion_check(error_message, self.password_mismatched_error_message, self.password_mismatched_error_message_id)

    def click_register_button(self):
        Methods(self.driver).click_element(self.register_button_xp)

    def validate_register_action(self):
        element = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, self.registration_confirmation_message_xpath)))
    def perform_logout_action (self):
        Methods(self.driver).click_element(self.logout_linkText_xp)

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

        # verifying user name error message for empty case
        element_name = " user name "
        error_message =Methods(self.driver).get_error_messages(self.username_empty_case_error_message_id)
        Methods(self.driver).assertion_check(error_message, self.username_empty_case_error_message, element_name)

        # verifying password error message for empty case
        element_name = " password "
        error_message = Methods(self.driver).get_error_messages(self.password_empty_case_error_message_id)
        Methods(self.driver).assertion_check(error_message, self.password_empty_case_error_message, element_name)

        # verifying password error message for empty case
        element_name = " confirm password "
        error_message = Methods(self.driver).get_error_messages(self.confirm_password_empty_case_error_message_id)
        Methods(self.driver).assertion_check(error_message, self.confirm_password_empty_case_error_message, element_name)

    def enter_valid_data_in_register_form(self):

        first_name = fake.first_name()
        last_name = fake.last_name()
        ssn = fake.ssn()
        street_name = fake.street_name()
        city_name = fake.city()
        state_name = fake.city()
        phone_number = fake.phone_number()
        zip_code = fake.postcode()
        user_name = fake.name().replace(" ","")
        password = fake.password()
        print(user_name,password,first_name,last_name,street_name,city_name,state_name,ssn,zip_code,phone_number)

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

        # Entering valid data in phone number
        Methods(self.driver).enter_data_id(self.address_PhoneNumber_input_field_id, phone_number)
        time.sleep(2)

        # Entering valid data in ssn
        Methods(self.driver).enter_data_id(self.customer_ssn_input_field_id, ssn)
        time.sleep(2)

        # Entering valid data in username field
        Methods(self.driver).enter_data_id(self.username_input_field_id, user_name)
        time.sleep(2)

        # Entering valid data in password field
        Methods(self.driver).enter_data_id(self.password_input_field_id, password)
        time.sleep(2)

        # Entering valid data in confirm password field
        Methods(self.driver).enter_data_id(self.confirm_password_input_field_id, password)
        time.sleep(2)
        self.save_data_in_array(user_name,password,first_name,last_name,street_name,city_name,state_name,ssn,zip_code,phone_number)

    def save_data_in_array(self,user_name,password,first_name,last_name,street_name,city_name,state_name,ssn,zip_code,phone_number):

        profile_details_array = []
        main_array = []
        profile_details_array.append(first_name)
        profile_details_array.append(last_name)
        profile_details_array.append(street_name)
        profile_details_array.append(city_name)
        profile_details_array.append(state_name)
        profile_details_array.append(phone_number)
        profile_details_array.append(zip_code)
        profile_details_array.append(ssn)
        profile_details_array.append(user_name)
        profile_details_array.append(password)

        print(profile_details_array)
        main_array.append(profile_details_array)
        print( " This is the details of main array")
        print(main_array)
        self.profile_array_list = main_array

    def save_data_in_csv_file(self,arraylist):

        with open("profile_data.csv", "a", newline="") as f:
            # creating the writer
            writer = csv.writer(f)
            writer.writerows(arraylist)

    def enter_in_valid_data_in_confirm_password_register_form(self):
        first_name = fake.first_name()
        last_name = fake.last_name()
        ssn = fake.ssn()
        street_name = fake.street_name()
        city_name = fake.city()
        state_name = fake.city()
        phone_number = fake.phone_number()
        zip_code = fake.postcode()
        user_name = fake.name().replace(" ", "")
        password = fake.password()
        print(first_name, last_name, ssn, street_name, city_name, zip_code, user_name, password)

        # Entering valid data in first name field
        Methods(self.driver).enter_data_id(self.firstName_input_field_id, first_name)
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

        # Entering valid data in phone number
        Methods(self.driver).enter_data_id(self.address_PhoneNumber_input_field_id, phone_number)
        time.sleep(2)

        # Entering valid data in ssn
        Methods(self.driver).enter_data_id(self.customer_ssn_input_field_id, ssn)
        time.sleep(2)

        # Entering valid data in username field
        Methods(self.driver).enter_data_id(self.username_input_field_id, user_name)
        time.sleep(2)

        # Entering valid data in password field
        Methods(self.driver).enter_data_id(self.password_input_field_id, password)
        time.sleep(2)

        # Entering valid data in confirm password field
        Methods(self.driver).enter_data_id(self.confirm_password_input_field_id, "password")
        time.sleep(2)