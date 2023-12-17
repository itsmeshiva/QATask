import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from faker import Faker
import csv

fake = Faker()


class Methods:
    profile_array_list = []
    def __init__(self, driver):
        self.driver = driver

    def assertion_check(self, received_message , required_message , field_name):

        if received_message == required_message :
            print("Error message in " + field_name + " is verified. Available error message is " + received_message)
            assert True

        else :
            print("Error message in " + field_name +  " is not verified. Available error message is " + received_message)
            assert False

    def validate_url(self, received_url , required_url , featureName):

        print(received_url,required_url)
        if required_url in received_url :

            print(featureName+ "'s" + "Url is verified")
            assert True

        else :
            print( featureName+ "'s " + "Url is not verified")
            assert False

    def get_error_messages(self,id):

        element = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.ID,id)))
        return element.text

    def click_element(self,xpath):

        element = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, xpath)))
        element.click()

    def enter_data_id(self,id,element_data):

        element = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.ID,id)))
        element.click()
        self.driver.execute_script("arguments[0].value = '" + element_data + "'", element)

    def enter_data_xpath(self, xpath , element_data):
        element = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable((By.XPATH,xpath)))
        element.click()
        self.driver.execute_script("arguments[0].value = '" + element_data + "'", element)

    def clear_element_data_using_id(self, id):
        element = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located((By.XPATH,id)))
        element.clear()


    def save_data_in_array(self,iterationNumber,firstname, lastname, street_name, city_name, state_name, phone_number, zip_code, ssn, user_name, password):

        profile_details_array = []
        profile_details_array.append(iterationNumber)
        profile_details_array.append(firstname)
        profile_details_array.append(lastname)
        profile_details_array.append(street_name)
        profile_details_array.append(city_name)
        profile_details_array.append(state_name)
        profile_details_array.append(phone_number)
        profile_details_array.append(zip_code)
        profile_details_array.append(ssn)
        profile_details_array.append(user_name)
        profile_details_array.append(password)

        print(profile_details_array)
        self.save_array_list(profile_details_array)


    def save_array_list(self, arraylist):
        self.profile_array_list = arraylist

    def save_data_in_csv_file(self,arraylist,loopCount):

        with open("A:\Automation Task Assignment\Assignment\Assignment\s.csv", "w") as f:

            for i in (loopCount):

                new_array = arraylist[i]
                # creating the writer
                writer = csv.writer(f)
                # using writerows, all rows at once
                writer.writerow(new_array)
