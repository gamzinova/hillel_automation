from Anna_Gamzinova.HW_18_framework_from_scratch.utilities.web_ui.base_page import BasePage
from Anna_Gamzinova.HW_18_framework_from_scratch.utilities import locators
from Anna_Gamzinova.HW_18_framework_from_scratch.page_objects.item_page import ItemPage
from Anna_Gamzinova.HW_18_framework_from_scratch.page_objects.cart_page import CartPage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_header_displayed(self):
        return self.is_displayed(locators.header)

    def select_first_item(self):
        return self.click(locators.first_item_page)

    def first_item_click(self):
        self.click(locators.first_item_page)
        return ItemPage(self._driver)

    def menu_click(self):
        self.click(locators.menu_button)
        return self

    def logout_click(self):
        self.click(locators.logout_button)
        return self

    def cart_click(self):
        self.click(locators.cart_button)
        return CartPage(self._driver)

    def add_to_cart_click(self):
        return self.click(locators.first_item_add_to_cart)

    def remove_from_cart(self):
        return self.click(locators.first_item_remove)

    def remove_item(self):
        return self.is_displayed(locators.first_item_remove)

    def menu_is_displayed(self):
        return self.is_displayed(locators.menu_bar)

    def products_banner(self):
        return self.is_displayed(locators.products_banner)
