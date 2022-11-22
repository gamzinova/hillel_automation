from Anna_Gamzinova.HW_18_framework_from_scratch.utilities.web_ui.base_page import BasePage
from Anna_Gamzinova.HW_18_framework_from_scratch.utilities import locators


class FinishPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_thanks_header(self):
        return self.is_displayed(locators.thanks_header)

    def label_picture(self):
        return self.is_displayed(locators.label_picture)

    def back_home_button(self):
        return self.click(locators.back_home_button)

