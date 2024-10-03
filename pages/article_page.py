from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from data.locators import ArticlePageLocators
import time

class ArticlePage(BasePage):

    def __init__(self, driver, wait):
        self.locator = ArticlePageLocators
        super().__init__(driver, wait)
        
    def upvote(self):
        # Wait for the <shreddit-post> element to be present
        shreddit_post = self.wait.until(
            EC.presence_of_element_located(self.locator.POST_TAG)
        )
        
        # Now find the <button> with the 'upvote' attribute inside the <shreddit-post>
        upvote_button = WebDriverWait(shreddit_post, 20).until(
            EC.presence_of_element_located(self.locator.UPVOTE_BTN)
        )
        # Click the upvote button
        upvote_button.click()

        # upvote_btn = self.wait.until(EC.element_to_be_clickable(self.locator.UPVOTE_BTN))
        # upvote_btn.click()
        return
    
    def downvote(self):
        # Wait for the <shreddit-post> element to be present
        shreddit_post = self.wait.until(
            EC.presence_of_element_located(self.locator.POST_TAG)
        )
        
        # Now find the <button> with the 'downvote' attribute inside the <shreddit-post>
        downvote_button = WebDriverWait(shreddit_post, 20).until(
            EC.presence_of_element_located(self.locator.DOWNVOTE_BTN)
        )
        
        # Click the downvote button
        downvote_button.click()
        return
