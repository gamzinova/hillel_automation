import pytest


@pytest.mark.regression
@pytest.mark.item_page
def test_item_click_opens_item_page(open_main_page):
    main_page = open_main_page
    item_page = main_page.first_item_click()
    assert item_page.is_picture_item() is True, "The item page has not been open"


@pytest.mark.regression
@pytest.mark.item_page
def test_back_to_products_from_item_page(init_main_page, open_item_page):
    main_page = init_main_page
    open_item_page.back_to_products_button()
    assert main_page.is_header_displayed() is True, "User was not forwarded to the new page"


@pytest.mark.regression
@pytest.mark.item_page
def test_remove_item_from_cart_item_page(open_item_page):
    item_page = open_item_page.add_to_cart_button().remove_from_cart_item_page()
    assert item_page.is_add_to_cart_button() is True, "Can't remove item"


@pytest.mark.regression
@pytest.mark.item_page
def test_logout_from_item_page(open_item_page, open_login_page):
    open_item_page.menu_click().logout_click()
    login_page = open_login_page
    assert login_page.is_login_button_displayed() is True, "User has not logged out"


@pytest.mark.regression
@pytest.mark.item_page
def test_open_cart(open_item_page):
    item_page = open_item_page
    cart_page = item_page.cart_click()
    assert cart_page.is_cart_item() is True, "The cart page has not been open"


@pytest.mark.regression
@pytest.mark.item_page
def test_add_item_to_cart_item_page(open_item_page):
    item_page = open_item_page.add_to_cart_button()
    assert item_page.is_remove_item() is True, "Can't add item"
