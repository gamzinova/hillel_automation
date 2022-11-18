import xpath_and_css_locators as locator
import configurations
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login():
    chrome_driver = Chrome("chromedriver.exe")
    wait = WebDriverWait(chrome_driver, 20)
    chrome_driver.maximize_window()
    chrome_driver.get(configurations.website_url)
    username_input_element = wait.until(EC.presence_of_element_located((By.XPATH, locator.username_input)))
    username_input_element.send_keys(configurations.user_name)
    password_input_element = wait.until(EC.presence_of_element_located((By.XPATH, locator.password_input)))
    password_input_element.send_keys(configurations.password)
    login_button_element = wait.until(EC.element_to_be_clickable((By.XPATH, locator.login_button)))
    login_button_element.click()
    header_element = chrome_driver.find_element(By.XPATH, locator.header)
    is_header = header_element.is_displayed()
    assert is_header is True, "User was not logged-in"
