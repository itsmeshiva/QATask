import os
from pathlib import Path
import configparser

path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config_path = os.path.join(ROOT_DIR, r"..\Config\config.ini")

config = configparser.RawConfigParser()
config.read(config_path)


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('info', 'url_application')
        return url

    @staticmethod
    def get_registration_page_url():
        url = config.get('info', 'url_register_page')
        return url

    @staticmethod
    def get_about_us_url():
        url = config.get('info', 'url_about_us_page')
        return url

    @staticmethod
    def get_services_url():
        url = config.get('info', 'url_services_page')
        return url

    @staticmethod
    def get_products_url():
        url = config.get('info', 'url_products_page')
        return url

    @staticmethod
    def get_locations_url():
        url = config.get('info', 'url_locations_page')
        return url

    @staticmethod
    def get_forum_url():
        url = config.get('info', 'url_forum_page')
        return url

    @staticmethod
    def get_site_map_url():
        url = config.get('info', 'url_site_map_page')
        return url

    @staticmethod
    def get_contact_us_url():
        url = config.get('info', 'url_contact_us_page')
        return url

    @staticmethod
    def get_forgot_info_url():
        url = config.get('info', 'url_forgot_info_page')
        return url
