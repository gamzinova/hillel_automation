from Anna_Gamzinova.HW_18_framework_from_scratch.utilities.web_ui.base_page import BasePage
from Anna_Gamzinova.HW_18_framework_from_scratch.utilities import locators


class ItemPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def picture_item(self):
        return self.is_displayed(locators.picture_item)

    def back_to_products_button(self):
        self.click(locators.back_to_products_button)
        return self

    def add_to_cart_button(self):
        self.click(locators.add_to_cart_button)
        return self

    def is_add_to_cart_button(self):
        return self.is_displayed(locators.add_to_cart_button)

    def remove_from_cart_item_page(self):
        self.click(locators.remove_the_item_item_page)
        return self

    def remove_item(self):
        return self.is_displayed(locators.remove_the_item_item_page)
