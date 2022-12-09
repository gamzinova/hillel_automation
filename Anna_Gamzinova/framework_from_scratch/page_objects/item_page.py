from __future__ import annotations

from Anna_Gamzinova.framework_from_scratch.page_objects.cart_page import CartPage
from Anna_Gamzinova.framework_from_scratch.utilities.web_ui.base_page import BasePage
from Anna_Gamzinova.framework_from_scratch.locators import xpath_locators
from Anna_Gamzinova.framework_from_scratch.utilities.decorators import auto_add_step


@auto_add_step
class ItemPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_picture_item(self) -> bool:
        return self.is_displayed(xpath_locators.picture_item)

    def back_to_products_button(self) -> ItemPage:
        self.click(xpath_locators.back_to_products_button)
        return self

    def add_to_cart_button(self) -> ItemPage:
        self.click(xpath_locators.add_to_cart_button)
        return self

    def is_add_to_cart_button(self) -> bool:
        return self.is_displayed(xpath_locators.add_to_cart_button)

    def remove_from_cart_item_page(self) -> ItemPage:
        self.click(xpath_locators.remove_the_item_item_page)
        return self

    def is_remove_item(self) -> bool:
        return self.is_displayed(xpath_locators.remove_the_item_item_page)

    def menu_click(self) -> ItemPage:
        self.click(xpath_locators.menu_button)
        return self

    def logout_click(self) -> LoginPage:
        self.click(xpath_locators.logout_button)
        return self

    def cart_click(self) -> CartPage:
        self.click(xpath_locators.cart_button)
        return CartPage(self._driver)
