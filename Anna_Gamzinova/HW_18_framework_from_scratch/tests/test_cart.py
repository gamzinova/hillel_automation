import pytest
from Anna_Gamzinova.HW_18_framework_from_scratch.utilities.config_parser import ReadConfig


@pytest.mark.regression
@pytest.mark.cart
def test_item_in_the_cart(open_main_page):
    main_page = open_main_page
    main_page.add_to_cart_click()
    cart_page = main_page.cart_click()
    assert cart_page.first_item_in_the_cart() is True, "The item has not been added"


@pytest.mark.regression
@pytest.mark.cart
def test_remove_item_from_cart(open_cart_page_with_item):
    cart_page = open_cart_page_with_item
    cart_page.remove_item_from_the_cart()
    assert cart_page.first_item_in_the_cart() is False, "The item has not been removed"


@pytest.mark.regression
@pytest.mark.cart
def test_continue_shopping(init_main_page, open_cart_page_with_item):
    main_page = init_main_page
    open_cart_page_with_item.continue_shopping_button()
    assert main_page.products_banner() is True, "You haven't been forwarded to the main page"


@pytest.mark.regression
@pytest.mark.cart
def test_logout_from_cart(open_cart_page_with_item, open_login_page):
    open_cart_page_with_item.menu_click().logout_click()
    login_page = open_login_page
    assert login_page.login_button_displayed() is True, "User has not logged out"


@pytest.mark.regression
@pytest.mark.cart
def test_checkout(open_cart_page_with_item):
    checkout_page = open_cart_page_with_item.checkout_button_click()
    assert checkout_page.first_name_info() is True, "User has not been forwarded to checkout page"


@pytest.mark.regression
@pytest.mark.cart
def test_set_values_and_continue(open_checkout_page):
    overview_page = open_checkout_page. \
        set_checkout_info(ReadConfig.get_first_name(), ReadConfig.get_last_name(), ReadConfig.get_zip()). \
        click_continue_button()
    assert overview_page.payment_information() is True, "User has not been forwarded to overview page"


@pytest.mark.regression
@pytest.mark.cart
def test_empty_checkout_info_error(open_checkout_page):
    checkout_page = open_checkout_page.continue_button_no_values()
    assert checkout_page.error_message_checkout() is True, "User was able to checkout"


@pytest.mark.regression
@pytest.mark.cart
def test_cancel_checkout(init_main_page, open_checkout_page):
    main_page = init_main_page
    open_checkout_page.cancel_checkout_button()
    assert main_page.products_banner() is True, "You haven't been forwarded to the main page"



