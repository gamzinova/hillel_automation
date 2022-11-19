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
