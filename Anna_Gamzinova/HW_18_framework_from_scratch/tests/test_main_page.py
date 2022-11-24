import pytest


@pytest.mark.regression
@pytest.mark.main_page
def test_menu(open_main_page):
    main_page = open_main_page
    main_page.menu_click()
    assert main_page.is_menu_is_displayed() is True, "The menu has not been open"


@pytest.mark.regression
@pytest.mark.main_page
def test_logout(open_main_page, open_login_page):
    main_page = open_main_page
    main_page.menu_click().logout_click()
    login_page = open_login_page
    assert login_page.is_login_button_displayed() is True, "user has not logged out"


@pytest.mark.regression
@pytest.mark.main_page
def test_open_cart(open_main_page):
    main_page = open_main_page
    cart_page = main_page.cart_click()
    assert cart_page.is_cart_item() is True, "The cart page has not been open"


@pytest.mark.regression
@pytest.mark.main_page
def test_add_item_to_cart_remove_check(open_main_page):
    main_page = open_main_page
    main_page.add_to_cart_click()
    assert main_page.is_remove_item() is True, "Can't remove item"
