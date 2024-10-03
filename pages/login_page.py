from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from data.locators import LoginPageLocators
import time

class LoginPage(BasePage):

    def __init__(self, driver, wait):
        self.url = "https://www.reddit.com"
        self.locator = LoginPageLocators
        super().__init__(driver, wait)

    def login(self, username, password, link):
        self.url = link
        self.go_to_page(self.url)
        
        login_link = self.wait.until(EC.element_to_be_clickable(self.locator.LOGIN_LINK))
        login_link.click()
        
        username_input = self.wait.until(EC.presence_of_element_located(self.locator.USERNAME_INPUT))
        username_input.click()
        username_input.send_keys(username)
        
        password_input = self.wait.until(EC.presence_of_element_located(self.locator.PASSWORD_INPUT))
        password_input.click()
        password_input.send_keys(password)
        
        time.sleep(3)
        password_input.send_keys(Keys.ENTER)
        time.sleep(3)
        
    def logout(self):
        expand_userdrawer_item = self.wait.until(EC.element_to_be_clickable(self.locator.EXPAND_USERDRAWER_ITEM))
        expand_userdrawer_item.click()
        
        logout_item = self.wait.until(EC.element_to_be_clickable(self.locator.LOGOUT_ITEM))
        logout_item.click()
        