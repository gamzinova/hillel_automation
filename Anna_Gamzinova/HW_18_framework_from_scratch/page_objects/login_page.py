from Anna_Gamzinova.HW_18_framework_from_scratch.page_objects.main_page import MainPage
from Anna_Gamzinova.HW_18_framework_from_scratch.utilities import locators
from Anna_Gamzinova.HW_18_framework_from_scratch.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def set_username(self, username_value):
        self.send_keys(locators.username_input, username_value)
        return self

    def set_password(self, password_value):
        self.send_keys(locators.password_input, password_value)
        return self

    def click_login_button(self):
        self.click(locators.login_button)
        return self

    def login(self, username_value, password_value):
        self.set_username(username_value).set_password(password_value).click_login_button()
        return MainPage(self._driver)

    def error_message_displayed(self):
        return self.is_displayed(locators.error_message)

    def login_button_displayed(self):
        return self.is_displayed(locators.login_button)
