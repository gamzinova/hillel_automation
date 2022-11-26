from __future__ import annotations
from Anna_Gamzinova.framework_from_scratch.utilities.web_ui.base_page import BasePage
from Anna_Gamzinova.framework_from_scratch.locators import xpath_locators
from Anna_Gamzinova.framework_from_scratch.page_objects.item_page import ItemPage
from Anna_Gamzinova.framework_from_scratch.page_objects.cart_page import CartPage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_header_displayed(self) -> bool:
        return self.is_displayed(xpath_locators.header)

    def select_first_item(self) -> ItemPage:
        self.click(xpath_locators.first_item_page)
        return ItemPage(self._driver)

    def first_item_click(self) -> ItemPage:
        self.click(xpath_locators.first_item_page)
        return ItemPage(self._driver)

    def menu_click(self) -> MainPage:
        self.click(xpath_locators.menu_button)
        return self

    def logout_click(self) -> MainPage:
        self.click(xpath_locators.logout_button)
        return self

    def cart_click(self) -> CartPage:
        self.click(xpath_locators.cart_button)
        return CartPage(self._driver)

    def add_to_cart_click(self) -> MainPage:
        self.click(xpath_locators.first_item_add_to_cart)
        return self

    def remove_from_cart(self) -> MainPage:
        self.click(xpath_locators.first_item_remove)
        return self

    def is_remove_item(self) -> bool:
        return self.is_displayed(xpath_locators.first_item_remove)

    def is_menu_is_displayed(self) -> bool:
        return self.is_displayed(xpath_locators.menu_bar)

    def is_products_banner(self) -> bool:
        return self.is_displayed(xpath_locators.products_banner)
