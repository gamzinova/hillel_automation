from __future__ import annotations
from Anna_Gamzinova.HW_18_framework_from_scratch.page_objects.overview_page import OverviewPage
from Anna_Gamzinova.HW_18_framework_from_scratch.utilities.web_ui.base_page import BasePage
from Anna_Gamzinova.HW_18_framework_from_scratch.locators import xpath_locators


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_checkout_form(self) -> bool:
        return self.is_displayed(xpath_locators.checkout_form)

    def is_first_name_info(self) -> bool:
        return self.is_displayed(xpath_locators.first_name_input)

    def set_first_name(self, first_name_value) -> CheckoutPage:
        self.send_keys(xpath_locators.first_name_input, first_name_value)
        return self

    def set_last_name(self, last_name_value) -> CheckoutPage:
        self.send_keys(xpath_locators.last_name_input, last_name_value)
        return self

    def set_zip_code(self, zip_code_value) -> CheckoutPage:
        self.send_keys(xpath_locators.zip_input, zip_code_value)
        return self

    def click_continue_button(self) -> OverviewPage:
        self.click(xpath_locators.continue_checkout_button)
        return OverviewPage(self._driver)

    def set_checkout_info(self, first_name_value, last_name_value, zip_code_value) -> CheckoutPage:
        self.set_first_name(first_name_value).set_last_name(last_name_value).set_zip_code(zip_code_value)
        return CheckoutPage(self._driver)

    def continue_button_no_values(self) -> CheckoutPage:
        self.click(xpath_locators.continue_checkout_button)
        return self

    def is_error_message_checkout(self) -> bool:
        return self.is_displayed(xpath_locators.error_message_checkout)

    def cancel_checkout_button(self) -> None:
        """
         A function that forwards the user to the Main page after clicking the cancel button on the checkout page
        """
        self.click(xpath_locators.cancel_button)

