from Anna_Gamzinova.HW_18_framework_from_scratch.utilities.web_ui.base_page import BasePage
from Anna_Gamzinova.HW_18_framework_from_scratch.utilities import locators


class OverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def payment_information(self):
        return self.is_displayed(locators.payment_information)

