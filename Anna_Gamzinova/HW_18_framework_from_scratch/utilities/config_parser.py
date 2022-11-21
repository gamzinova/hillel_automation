import configparser

config = configparser.RawConfigParser()
config.read(
    '/home/gamzinova/PycharmProjects/Automation/hillel_python_qa_homeworks_AG/Anna_Gamzinova/HW_18_framework_from_scratch/configurations/configurations.ini')


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
