from __future__ import annotations

from Anna_Gamzinova.framework_from_scratch.page_objects.checkout_page import CheckoutPage
from Anna_Gamzinova.framework_from_scratch.utilities.web_ui.base_page import BasePage
from Anna_Gamzinova.framework_from_scratch.locators import xpath_locators


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_cart_item(self) -> bool:
        return self.is_displayed(xpath_locators.cart_button)

    def is_first_item_in_the_cart(self) -> bool:
        return self.is_displayed(xpath_locators.cart_item)

    def remove_item_from_the_cart(self) -> CartPage:
        self.click(xpath_locators.remove_from_the_cart_button)
        return self

    def continue_shopping_button(self) -> CartPage:
        self.click(xpath_locators.continue_shopping_button)
        return self

    def menu_click(self) -> CartPage:
        self.click(xpath_locators.menu_button)
        return self

    def logout_click(self) -> CartPage:
        self.click(xpath_locators.logout_button)
        return self

    def checkout_button_click(self) -> CheckoutPage:
        self.click(xpath_locators.checkout_button)
        return CheckoutPage(self._driver)
