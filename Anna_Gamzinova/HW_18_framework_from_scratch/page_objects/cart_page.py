from Anna_Gamzinova.HW_18_framework_from_scratch.page_objects.checkout_page import CheckoutPage
from Anna_Gamzinova.HW_18_framework_from_scratch.utilities.web_ui.base_page import BasePage
from Anna_Gamzinova.HW_18_framework_from_scratch.utilities import locators


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def cart_item(self):
        return self.is_displayed(locators.cart_button)

    def first_item_in_the_cart(self):
        return self.is_displayed(locators.cart_item)

    def remove_item_from_the_cart(self):
        return self.click(locators.remove_from_the_cart_button)

    def continue_shopping_button(self):
        return self.click(locators.continue_shopping_button)

    def menu_click(self):
        self.click(locators.menu_button)
        return self

    def logout_click(self):
        self.click(locators.logout_button)
        return self

    def checkout_button_click(self):
        self.click(locators.checkout_button)
        return CheckoutPage
