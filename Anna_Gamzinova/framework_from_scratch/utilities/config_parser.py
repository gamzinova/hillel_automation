import configparser
from Anna_Gamzinova.framework_from_scratch.CONSTANTS import ROOT_DIR

config = configparser.RawConfigParser()
config.read(f'{ROOT_DIR}/configurations/configurations.ini')


class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_user_name():
        return config.get('user_info', 'user_name')

    @staticmethod
    def get_user_password():
        return config.get('user_info', 'password')

    @staticmethod
    def get_driver_id():
        return config.get('browser', 'browser_id')

    @staticmethod
    def get_first_name():
        return config.get('checkout_information', 'first_name')

    @staticmethod
    def get_last_name():
        return config.get('checkout_information', 'last_name')

    @staticmethod
    def get_zip():
        return config.get('checkout_information', 'zip')
