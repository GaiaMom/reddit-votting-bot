from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from data.locators import LoginPageLocators
import time


class LoginPage(BasePage):

    def __init__(self, driver, wait):
        self.locator = LoginPageLocators
        super().__init__(driver, wait)

    def login(self, username, password):
        login_link = self.wait.until(
            EC.element_to_be_clickable(self.locator.LOGIN_LINK)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", login_link)
        login_link.click()

        username_input = self.wait.until(
            EC.element_to_be_clickable(self.locator.USERNAME_INPUT)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", username_input)
        username_input.click()
        username_input.clear()
        username_input.send_keys(username)

        password_input = self.wait.until(
            EC.element_to_be_clickable(self.locator.PASSWORD_INPUT)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", password_input)
        password_input.click()
        password_input.clear()
        password_input.send_keys(password)

        time.sleep(10)
        password_input.send_keys(Keys.ENTER)

    def logout(self):
        expand_userdrawer_item = self.wait.until(
            EC.element_to_be_clickable(self.locator.EXPAND_USERDRAWER_ITEM)
        )
        expand_userdrawer_item.click()

        logout_item = self.wait.until(
            EC.element_to_be_clickable(self.locator.LOGOUT_ITEM)
        )
        logout_item.click()
