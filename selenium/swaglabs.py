from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SwagLabs:

    # Locators for UI interactions:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@class='btn_action' and @id='login-button']")
    BOT_IMAGE = (By.CLASS_NAME, "bot_column")
    PEEK_ICON = (By.CSS_SELECTOR, ".peek")

    # SwagLabs URL:
    URL = "https://www.saucedemo.com/v1/"

    def __init__(self, browser):
        self.browser = browser

    # Open URL method
    def open_url(self):
        try:
            self.browser.get(self.URL)
        except Exception as e:
            print("SwagLabs website cannot be opened, reason: ", e)

    def is_bot_image_visible(self):
        bot_image = WebDriverWait(self.browser, 12).until(
            EC.visibility_of_element_located(self.BOT_IMAGE))
        if bot_image:
            return True

    def is_peekicon_image_visible(self):
        peek_icon = WebDriverWait(self.browser, 12).until(
            EC.visibility_of_element_located(self.PEEK_ICON))
        if peek_icon:
            return True

    def fill_username(self, user_name):
        username = self.browser.find_element(*self.USERNAME)
        username.send_keys(user_name)

    def fill_password(self, pass_word):
        password = self.browser.find_element(*self.PASSWORD)
        password.send_keys(pass_word)

    def login_to_swaglabs(self):
        login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        login_button.click()