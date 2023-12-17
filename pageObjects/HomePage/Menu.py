import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Methods.methods import Methods
from selenium.webdriver.support import expected_conditions as ec
from faker import Faker
import csv

fake = Faker()


class MenuAction:

    def __init__(self, driver):
        self.driver = driver

    home_linkText_xp = "//a[contains(text(),'Home')]"
    about_us_linkText_xp = "//a[contains(text(),'About Us')]"
    products_linkText_xp = "//a[contains(text(),'Products')]"
    locations_us_linkText_xp = "//a[contains(text(),'Locations')]"
    forum_linkText_xp = "//a[contains(text(),'Forum')]"
    site_map_linkText_xp = "//a[contains(text(),'Site Map')]"
    contact_us_linkText_xp = "//a[contains(text(),'Contact Us')]"
    service_linkText_xp = "//a[contains(text(),'Service')]"

    def click_home_menu (self):
        Methods(self.driver).click_element(self.home_linkText_xp)

    def click_about_us_menu (self):
        Methods(self.driver).click_element(self.about_us_linkText_xp)

    def click_services_menu (self):
        Methods(self.driver).click_element(self.service_linkText_xp)

    def click_products_menu (self):
        Methods(self.driver).click_element(self.products_linkText_xp)

    def click_locations_menu(self):
        Methods(self.driver).click_element(self.locations_us_linkText_xp)

    def click_forum_menu(self):
        Methods(self.driver).click_element(self.forum_linkText_xp)

    def click_site_map_menu(self):
        Methods(self.driver).click_element(self.site_map_linkText_xp)

    def click_contact_us_menu (self):
        Methods(self.driver).click_element(self.contact_us_linkText_xp)

    def validate_menu_page_url(self, required_url , MenuName):
        received_url = self.driver.current_url
        Methods(self.driver).validate_url(received_url, required_url ,MenuName )