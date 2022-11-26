from __future__ import annotations

from Anna_Gamzinova.framework_from_scratch.utilities.web_ui.base_page import BasePage
from Anna_Gamzinova.framework_from_scratch.locators import xpath_locators


class FinishPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_thanks_header(self) -> bool:
        return self.is_displayed(xpath_locators.thanks_header)

    def is_label_picture(self) -> bool:
        return self.is_displayed(xpath_locators.label_picture)

    def back_home_button(self) -> MainPage:
        self.click(xpath_locators.back_home_button)
        return MainPage(self._driver)
