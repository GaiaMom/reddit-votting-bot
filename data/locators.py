from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[@href='https://www.reddit.com/login/']")
    USERNAME_INPUT = (By.ID, "login-username")
    PASSWORD_INPUT = (By.ID, "login-password")
    POPUP_LOGIN_BTN = (By.XPATH, "//button")
    EXPAND_USERDRAWER_ITEM = (By.ID, "expand-user-drawer-button")
    LOGOUT_ITEM = (By.ID, "logout-list-item")

class ArticlePageLocators:
    POST_TAG = (By.TAG_NAME, "shreddit-post")
    UPVOTE_BTN = (By.CSS_SELECTOR, "button[upvote]")
    DOWNVOTE_BTN = (By.CSS_SELECTOR, "button[downvote]")