import pytest
from Anna_Gamzinova.HW_18_framework_from_scratch.utilities.config_parser import ReadConfig


@pytest.mark.login_page
def test_login(open_login_page):
    login_page = open_login_page
    main_page = login_page.login(ReadConfig.get_user_name(), ReadConfig.get_user_password())
    assert main_page.is_header_displayed() is True, "User was not logged-in"


@pytest.mark.login_page
@pytest.mark.parametrize('username_value, password_value', [('', ''), ('test', f'{ReadConfig.get_user_password()}'),
                                                            (f'{ReadConfig.get_user_name()}', 'test')],
                         ids=["no values", "wrong username", "wrong password"])
def test_login_invalid(open_login_page, username_value, password_value):
    login_page = open_login_page
    login_page.set_username(username_value).set_password(password_value).click_login_button()
    assert login_page.error_message_displayed() is True, "User has logged in "


@pytest.mark.main_page
def test_menu(open_main_page):
    main_page = open_main_page
    main_page.menu_click()
    assert main_page.menu_is_displayed() is True, "The menu has not been open"


@pytest.mark.main_page
def test_logout(open_main_page, open_login_page):
    main_page = open_main_page
    main_page.menu_click().logout_click()
    login_page = open_login_page
    assert login_page.login_button_displayed() is True, "user has not logged out"


@pytest.mark.item_page
def test_item_click_opens_item_page(open_main_page):
    main_page = open_main_page
    item_page = main_page.first_item_click()
    assert item_page.picture_item() is True, "The item page has not been open"


@pytest.mark.main_page
def test_open_cart(open_main_page):
    main_page = open_main_page
    cart_page = main_page.cart_click()
    assert cart_page.cart_item() is True, "The cart page has not been open"


@pytest.mark.main_page
def test_add_item_to_cart_remove_check(open_main_page):
    main_page = open_main_page
    main_page.add_to_cart_click()
    assert main_page.remove_item() is True, "Can't remove item"


@pytest.mark.cart_page
def test_item_in_the_cart(open_main_page):
    main_page = open_main_page
    main_page.add_to_cart_click()
    cart_page = main_page.cart_click()
    assert cart_page.first_item_in_the_cart() is True, "The item has not been added"


@pytest.mark.cart_page
def test_remove_item_from_cart(open_cart_page_with_item):
    cart_page = open_cart_page_with_item
    cart_page.remove_item_from_the_cart()
    assert cart_page.first_item_in_the_cart() is False, "The item has not been removed"


# TODO
@pytest.mark.cart_page
def test_continue_shopping(open_cart_page_with_item):
    cart_page = open_cart_page_with_item
    main_page = cart_page.continue_shopping_button()
    assert main_page.products_banner() is True, "You haven't been forwarded to the main page"


@pytest.mark.cart_page
def test_logout_from_cart(open_cart_page_with_item, open_login_page):
    cart_page = open_cart_page_with_item
    cart_page.menu_click().logout_click()
    login_page = open_login_page
    assert login_page.login_button_displayed() is True, "User has not logged out"


@pytest.mark.cart_page
# TODO
def test_checkout(open_cart_page_with_item):
    checkout_page = open_cart_page_with_item.checkout_button_click()
    assert checkout_page.first_name_info() is True, "User has not been forwarded to checkout page"


# TODO
@pytest.mark.cart_page
def test_set_values_and_continue(open_checkout_page):
    checkout_page = open_checkout_page
    checkout_page.set_checkout_info(ReadConfig.get_first_name(), ReadConfig.get_last_name(), ReadConfig.get_zip())
    overview_page = checkout_page.click_continue_button()
    assert overview_page.payment_information() is True, "User has not been forwarded to overview page"


# TODO
@pytest.mark.cart_page
def test_empty_checkout_info_error(open_checkout_page):
    checkout_page = open_checkout_page
    checkout_page.continue_button_no_values()
    assert checkout_page.error_message_checkout() is True, "User was able to checkout"

# TODO
@pytest.mark.cart_page
def test_cancel_checkout(open_checkout_page):
    checkout_page = open_checkout_page
    main_page = checkout_page.cancel_checkout_button()
    assert main_page.products_banner() is True, "You haven't been forwarded to the main page"
