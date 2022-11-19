from Anna_Gamzinova.HW_18_framework_from_scratch.utilities.web_ui.base_page import BasePage
from Anna_Gamzinova.HW_18_framework_from_scratch.utilities import locators


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def cart_item(self):
        return self.is_displayed(locators.cart_button)
