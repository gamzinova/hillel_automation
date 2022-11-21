import pytest

from Anna_Gamzinova.HW_18_framework_from_scratch.page_objects.login_page import LoginPage
from Anna_Gamzinova.HW_18_framework_from_scratch.utilities.config_parser import ReadConfig
from Anna_Gamzinova.HW_18_framework_from_scratch.utilities.driver_factory import DriverFactory


@pytest.fixture(scope='session')
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
    login_page = open_login_page
    main_page = login_page.login(ReadConfig.get_user_name(), ReadConfig.get_user_password())
    return main_page


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


