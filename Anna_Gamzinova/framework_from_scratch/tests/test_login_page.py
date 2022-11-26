import pytest
from Anna_Gamzinova.framework_from_scratch.utilities.config_parser import ReadConfig


@pytest.mark.regression
@pytest.mark.login_page
@pytest.mark.parametrize('username_value, password_value', [('', ''), ('test', f'{ReadConfig.get_user_password()}'),
                                                            (f'{ReadConfig.get_user_name()}', 'test'),
                                                            ('', f'{ReadConfig.get_user_password()}'),
                                                            (f'{ReadConfig.get_user_name()}', '')],
                         ids=["no values", "wrong username", "wrong password", "empty username,correct password",
                              "correct username, empty password"])
def test_login_invalid(open_login_page, username_value, password_value):
    login_page = open_login_page
    login_page.set_username(username_value).set_password(password_value).click_login_button()
    assert login_page.is_error_message_displayed() is True, "User has logged in "


@pytest.mark.regression
@pytest.mark.login_page
@pytest.mark.parametrize('username_value, password_value', [('', f'{ReadConfig.get_user_password()}')],
                         ids=["empty username,correct password"])
def test_login_invalid(open_login_page, username_value, password_value):
    login_page = open_login_page
    login_page.set_username(username_value).set_password(password_value).click_login_button()
    assert login_page.is_empty_values_error_message_displayed() is True, "User has logged in "


@pytest.mark.regression
@pytest.mark.login_page
def test_login(open_login_page, env):
    login_page = open_login_page
    main_page = login_page.login(env.user_name, env.password)
    assert main_page.is_header_displayed() is True, "User was not logged-in"


@pytest.mark.regression
@pytest.mark.smoke
def test_finish_checkout(open_overview_page):
    """
    A test that tests all the flow from login to buying the product.
    """
    finish_page = open_overview_page.finish_button()
    assert finish_page.is_thanks_header() is True, "You were not able to buy a product"
