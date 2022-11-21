from Anna_Gamzinova.HW_18_framework_from_scratch.page_objects.overview_page import OverviewPage
from Anna_Gamzinova.HW_18_framework_from_scratch.utilities.web_ui.base_page import BasePage
from Anna_Gamzinova.HW_18_framework_from_scratch.utilities import locators


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def checkout_form(self):
        return self.is_displayed(locators.checkout_form)

    def first_name_info(self):
        return self.is_displayed(locators.first_name_input)

    def set_first_name(self, first_name_value):
        self.send_keys(locators.first_name_input, first_name_value)
        return self

    def set_last_name(self, last_name_value):
        self.send_keys(locators.last_name_input, last_name_value)
        return self

    def set_zip_code(self, zip_code_value):
        self.send_keys(locators.zip_input, zip_code_value)
        return self

    def click_continue_button(self):
        self.click(locators.continue_checkout_button)
        return OverviewPage(self._driver)

    def set_checkout_info(self, first_name_value, last_name_value, zip_code_value):
        self.set_first_name(first_name_value).set_last_name(last_name_value).set_zip_code(zip_code_value)
        return CheckoutPage

    def continue_button_no_values(self):
        self.click(locators.continue_checkout_button)
        return self

    def error_message_checkout(self):
        return self.is_displayed(locators.error_message_checkout)

    def cancel_checkout_button(self):
        return self.click(locators.cancel_button)

