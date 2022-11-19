import pytest
from Anna_Gamzinova.HW_18_framework_from_scratch.utilities.config_parser import ReadConfig


def test_login(open_login_page):
    login_page = open_login_page
    main_page = login_page.login(ReadConfig.get_user_name(), ReadConfig.get_user_password())
    assert main_page.is_header_displayed() is True, "User was not logged-in"


@pytest.mark.parametrize('username_value, password_value', [('', ''), ('test', f'{ReadConfig.get_user_password()}'),
                                                            (f'{ReadConfig.get_user_name()}', 'test')],
                         ids=["no values", "wrong username", "wrong password"])
def test_login_invalid(open_login_page, username_value, password_value):
    login_page = open_login_page
    login_page.set_username(username_value).set_password(password_value).click_login_button()
    assert login_page.error_message_displayed() is True, "User has logged in "


def test_menu(open_main_page):
    main_page = open_main_page
    main_page.menu_click()
    assert main_page.menu_is_displayed() is True, "The menu has not been open"


def test_logout(open_main_page, open_login_page):
    main_page = open_main_page
    main_page.menu_click().logout_click()
    login_page = open_login_page
    assert login_page.login_button_displayed() is True, "user has not logged out"


def test_item_click_opens_item_page(open_main_page):
    main_page = open_main_page
    item_page = main_page.first_item_click()
    assert item_page.picture_item() is True, "The item page has not been open"


def test_open_cart(open_main_page):
    main_page = open_main_page
    cart_page = main_page.cart_click()
    assert cart_page.cart_item() is True, "The cart page has not been open"


def test_add_item_to_cart_remove_check(open_main_page):
    main_page = open_main_page
    main_page.add_to_cart_click()
    assert main_page.remove_item() is True, "Can't remove item"
