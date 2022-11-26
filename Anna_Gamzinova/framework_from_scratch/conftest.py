import pytest
import json

from Anna_Gamzinova.framework_from_scratch.CONSTANTS import ROOT_DIR
from Anna_Gamzinova.framework_from_scratch.page_objects.main_page import MainPage
from Anna_Gamzinova.framework_from_scratch.page_objects.login_page import LoginPage
from Anna_Gamzinova.framework_from_scratch.utilities.config_parser import ReadConfig
from Anna_Gamzinova.framework_from_scratch.utilities.configurations import Configurations
from Anna_Gamzinova.framework_from_scratch.utilities.driver_factory import DriverFactory


@pytest.fixture()
def env():
    with open(f'{ROOT_DIR}/configurations/configurations.json') as file:
        env_dict = json.loads(file.read())
    return Configurations(**env_dict)


@pytest.fixture()
def create_driver():
    driver = DriverFactory.create_driver(driver_id=ReadConfig.get_driver_id())
    driver.maximize_window()
    driver.get(ReadConfig.get_base_url())
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def open_main_page(open_login_page):
    """
    A fixture that opens a main page after login
    """
    return open_login_page.login(ReadConfig.get_user_name(), ReadConfig.get_user_password())


@pytest.fixture()
def init_main_page(create_driver):
    """
    Initialize a main page object
    """
    return MainPage(create_driver)


@pytest.fixture()
def open_cart_page(open_main_page):
    cart_page = open_main_page.cart_click()
    return cart_page


@pytest.fixture()
def open_cart_page_with_item(open_main_page):
    main_page = open_main_page
    main_page.add_to_cart_click()
    cart_page = main_page.cart_click()
    return cart_page


@pytest.fixture()
def open_checkout_page(open_cart_page_with_item):
    cart_page = open_cart_page_with_item
    checkout_page = cart_page.checkout_button_click()
    return checkout_page


@pytest.fixture()
def open_item_page(open_main_page):
    item_page = open_main_page.first_item_click()
    return item_page


@pytest.fixture()
def open_overview_page(open_checkout_page):
    checkout_page = open_checkout_page
    checkout_page.set_checkout_info(ReadConfig.get_first_name(), ReadConfig.get_last_name(), ReadConfig.get_zip())
    overview_page = checkout_page.click_continue_button()
    return overview_page
