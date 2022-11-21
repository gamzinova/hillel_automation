from selenium.webdriver.common.by import By

# website:https://www.saucedemo.com/

# Xpath
# page: login page
username_input = (By.XPATH, '//*[@id="user-name"]')
password_input = (By.XPATH, '//*[@id="password"]')
login_button = (By.XPATH, '//*[@id="login-button"]')
error_message = (By.XPATH, '//*[@data-test="error"]')

# main page:
header = (By.XPATH, '//*[@class="app_logo"]')
products_banner = (By.XPATH, '//*[@class="title"]')
menu_button = (By.XPATH, '//*[@id="react-burger-menu-btn"]')
menu_bar = (By.XPATH, '//*[@class="bm-item-list"]')
logout_button = (By.XPATH, '//*[@id="logout_sidebar_link"]')
cart_button = (By.XPATH, '//*[@class="shopping_cart_link"]')
filter_button = (By.XPATH, '//*[@class="product_sort_container"]')
filter_AZ = (By.XPATH, '//*[@value="az"]')
first_item_page = (By.XPATH, '//*[@alt="Sauce Labs Backpack"]')
first_item_add_to_cart = (By.XPATH, '//*[@name="add-to-cart-sauce-labs-backpack"]')
first_item_remove = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')

# item page:
back_to_products_button = (By.XPATH, '//*[@id="back-to-products"]')
picture_item = (By.XPATH, '//*[@alt="Sauce Labs Backpack"]')
add_to_cart_button = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')

# cart page
remove_from_the_cart_button = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
continue_shopping_button = (By.XPATH, '//*[@id="continue-shopping"]')
checkout_button = (By.XPATH, '//*[@id="checkout"]')
item_in_the_cart = (By.XPATH, '//*[@class="inventory_item_name"]')
cart_item = (By.XPATH, '//*[@class="cart_item_label"]')

# checkout page:
first_name_input = (By.XPATH, '//*[@id="first-name"]')
last_name_input = (By.XPATH, '//*[@id="last-name"]')
zip_input = (By.XPATH, '//*[@id="postal-code"]')
cancel_button = (By.XPATH, '//*[@id="cancel"]')
continue_checkout_button = (By.XPATH, '//*[@id="continue"]')
checkout_form = (By.XPATH, '//*[@class="checkout_info"]')
error_message_checkout = (By.XPATH, '//*[@data-test="error"]')

# checkout overview page:
cart_item = (By.XPATH, '//*[@class="inventory_item_name"]')
payment_information = (By.XPATH, '//*[@class="summary_value_label"]')
total_price = (By.XPATH, '//*[@class="summary_total_label"]')
cancel = (By.XPATH, '//*[@id="cancel"]')
finish = (By.XPATH, '//*[@id="finish"]')

# checkout finish page:
thanks_header = (By.XPATH, '//*[@class="complete-header"]')
label_picture = (By.XPATH, '//*[@alt="Pony Express"]')
back_home_button = (By.XPATH, '//*[@id="back-to-products"]')

# footer:
twitter = (By.XPATH, '//*[@class="social_twitter"]')
facebook = (By.XPATH, '//*[@class="social_facebook"]')
linkedin = (By.XPATH, '//*[@class="social_linkedin"]')

# CSS
# website:https://www.saucedemo.com/

# page: login page
css_username_input = (By.CSS_SELECTOR, '#user-name')
css_password_input = (By.CSS_SELECTOR, '#password')
css_login_button = (By.CSS_SELECTOR, '#login-button')
css_error_message = (By.CSS_SELECTOR, '[data-test="error"]')

# main page:
css_menu_button = (By.CSS_SELECTOR, '#react-burger-menu-btn')
logout_button_menu = (By.CSS_SELECTOR, '# logout_sidebar_link')
css_cart_button = (By.CSS_SELECTOR, '[class="shopping_cart_link"]')
css_filter_button = (By.CSS_SELECTOR, '[class="product_sort_container"]')
css_filter_AZ = (By.CSS_SELECTOR, '[value="az"]')
css_first_item_page = (By.CSS_SELECTOR, '[alt="Sauce Labs Backpack"]')
css_first_item_add_to_cart = (By.CSS_SELECTOR, '[name="add-to-cart-sauce-labs-backpack"]')

# item page:
css_back_to_products_button = (By.CSS_SELECTOR, '#back-to-products')
css_item_picture = (By.CSS_SELECTOR, '[alt="Sauce Labs Backpack"]')
css_add_to_cart_button = (By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
css_remove_from_the_cart_button = (By.CSS_SELECTOR, '#remove-sauce-labs-backpack')
css_continue_shopping_button = (By.CSS_SELECTOR, '#continue-shopping')
css_checkout_button = (By.CSS_SELECTOR, '#checkout')
