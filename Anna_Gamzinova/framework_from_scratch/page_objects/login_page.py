from __future__ import annotations
from Anna_Gamzinova.framework_from_scratch.page_objects.main_page import MainPage
from Anna_Gamzinova.framework_from_scratch.locators import xpath_locators
from Anna_Gamzinova.framework_from_scratch.utilities.web_ui.base_page import BasePage
from Anna_Gamzinova.framework_from_scratch.utilities.decorators import auto_add_step


@auto_add_step
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def set_username(self, username_value) -> LoginPage:
        self.send_keys(xpath_locators.username_input, username_value)
        return self

    def set_password(self, password_value) -> LoginPage:
        self.send_keys(xpath_locators.password_input, password_value)
        return self

    def click_login_button(self) -> LoginPage:
        self.click(xpath_locators.login_button)
        return self

    def login(self, username_value, password_value) -> MainPage:
        self.set_username(username_value).set_password(password_value).click_login_button()
        return MainPage(self._driver)

    def is_error_message_displayed(self) -> bool:
        return self.is_displayed(xpath_locators.error_message)

    def is_login_button_displayed(self) -> bool:
        return self.is_displayed(xpath_locators.login_button)

    def is_empty_values_error_message_displayed(self) -> bool:
        return self.is_displayed(xpath_locators.empty_values)
