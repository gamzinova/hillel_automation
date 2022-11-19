from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 5)

    def wait_until_element_located(self, locator):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def wait_until_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def wait_until_element_visible(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def send_keys(self, locator, value, is_clear=True):
        element = self.wait_until_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def click(self, locator):
        element = self.wait_until_clickable(locator)
        element.click()

    def is_displayed(self, locator):
        try:
            self.wait_until_element_visible(locator)
            return True
        except TimeoutException:
            return False
