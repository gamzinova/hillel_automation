from Anna_Gamzinova.framework_from_scratch.page_objects.finish_page import FinishPage
from Anna_Gamzinova.framework_from_scratch.utilities.web_ui.base_page import BasePage
from Anna_Gamzinova.framework_from_scratch.locators import xpath_locators
from Anna_Gamzinova.framework_from_scratch.utilities.decorators import auto_add_step


@auto_add_step
class OverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_payment_information(self) -> bool:
        return self.is_displayed(xpath_locators.payment_information)

    def finish_button(self) -> FinishPage:
        self.click(xpath_locators.finish)
        return FinishPage(self._driver)
