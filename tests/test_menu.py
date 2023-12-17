
from faker import Faker
from utilities.readProperties import ReadConfig
from pageObjects.HomePage.Menu import MenuAction


class TestMenuFeature:

    application_url = ReadConfig.get_application_url()
    about_us_page_url = ReadConfig.get_about_us_url()
    site_map_page_url = ReadConfig.get_site_map_url()
    forum_page_url = ReadConfig.get_forum_url()
    location_page_url = ReadConfig.get_locations_url()
    product_page_url = ReadConfig.get_products_url()
    services_page_url = ReadConfig.get_services_url()
    def test_verifying_about_us_page_url(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.menuDriver = MenuAction(self.driver)
        self.menuDriver.click_about_us_menu()
        self.menuDriver.validate_menu_page_url( self.about_us_page_url,"About Us")
        self.driver.close()

    def test_verifying_home_page_url(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.menuDriver = MenuAction(self.driver)
        self.menuDriver.click_home_menu()
        self.menuDriver.validate_menu_page_url( self.application_url,"About Us")
        self.driver.close()

    def test_verifying_site_map_page_url(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.menuDriver = MenuAction(self.driver)
        self.menuDriver.click_site_map_menu()
        self.menuDriver.validate_menu_page_url( self.site_map_page_url,"Site Map")
        self.driver.close()

    def test_verifying_services_page_url(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.menuDriver = MenuAction(self.driver)
        self.menuDriver.click_services_menu()
        self.menuDriver.validate_menu_page_url( self.services_page_url,"Services")
        self.driver.close()

    def test_verifying_products_page_url(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.menuDriver = MenuAction(self.driver)
        self.menuDriver.click_products_menu()
        self.menuDriver.validate_menu_page_url( self.product_page_url,"Products")
        self.driver.close()

    def test_verifying_location_page_url(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.menuDriver = MenuAction(self.driver)
        self.menuDriver.click_locations_menu()
        self.menuDriver.validate_menu_page_url(self.location_page_url,"Location")
        self.driver.close()

    def test_verifying_forum_page_url(self, setup):
        self.driver = setup
        self.driver.get(self.application_url)
        self.driver.maximize_window()
        self.menuDriver = MenuAction(self.driver)
        self.menuDriver.click_forum_menu()
        self.menuDriver.validate_menu_page_url( self.forum_page_url,"Forum")
        self.driver.close()

