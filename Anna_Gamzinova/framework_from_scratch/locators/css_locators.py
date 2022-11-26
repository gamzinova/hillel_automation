from selenium.webdriver.common.by import By

# login page
css_username_input = (By.CSS_SELECTOR, '#user-name')
css_password_input = (By.CSS_SELECTOR, '#password')
css_login_button = (By.CSS_SELECTOR, '#login-button')
css_error_message = (By.CSS_SELECTOR, '[data-test="error"]')

# item page
css_back_to_products_button = (By.CSS_SELECTOR, '#back-to-products')
css_item_picture = (By.CSS_SELECTOR, '[alt="Sauce Labs Backpack"]')
css_add_to_cart_button = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
css_remove_from_the_cart_button = (By.CSS_SELECTOR, '#remove-sauce-labs-backpack')
css_continue_shopping_button = (By.CSS_SELECTOR, '#continue-shopping')
css_checkout_button = (By.CSS_SELECTOR, '#checkout')

# main_page
css_menu_button = (By.CSS_SELECTOR, '#react-burger-menu-btn')
logout_button_menu = (By.CSS_SELECTOR, '# logout_sidebar_link')
css_cart_button = (By.CSS_SELECTOR, '[class="shopping_cart_link"]')
css_filter_button = (By.CSS_SELECTOR, '[class="product_sort_container"]')
css_filter_AZ = (By.CSS_SELECTOR, '[value="az"]')
css_first_item_page = (By.CSS_SELECTOR, '[alt="Sauce Labs Backpack"]')
css_first_item_add_to_cart = (By.CSS_SELECTOR, '[name="add-to-cart-sauce-labs-backpack"]')
