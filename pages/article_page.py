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
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.TAG_NAME, "shreddit-overlay-display")
            )
        )

        # Wait for the <shreddit-post> element to be present
        shreddit_post = self.wait.until(
            EC.presence_of_element_located(self.locator.POST_TAG)
        )

        # Access the shadow root
        shadow_root = self.driver.execute_script(
            "return arguments[0].shadowRoot", shreddit_post
        )

        # # If the button is inside the shadow DOM, you'll need to retrieve it like this
        # upvote_button = shadow_root.find_element(By.CSS_SELECTOR, "button[upvote]")

        upvote_button = self.wait.until(
            lambda driver: shadow_root.find_element(By.CSS_SELECTOR, "button[upvote]")
        )
        aria_pressed_value = upvote_button.get_attribute("aria-pressed")
        if aria_pressed_value == "false":
            # Click the upvote button
            upvote_button.click()
        return

    def downvote(self):
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.TAG_NAME, "shreddit-overlay-display")
            )
        )

        # Wait for the <shreddit-post> element to be present
        shreddit_post = self.wait.until(
            EC.presence_of_element_located(self.locator.POST_TAG)
        )

        # Access the shadow root
        shadow_root = self.driver.execute_script(
            "return arguments[0].shadowRoot", shreddit_post
        )

        # # If the button is inside the shadow DOM, you'll need to retrieve it like this
        # downvote_button = shadow_root.find_element(By.CSS_SELECTOR, "button[downvote]")
        downvote_button = self.wait.until(
            lambda driver: shadow_root.find_element(By.CSS_SELECTOR, "button[downvote]")
        )

        aria_pressed_value = downvote_button.get_attribute("aria-pressed")
        if aria_pressed_value == "false":
            # Click the upvote button
            downvote_button.click()

        # Click the upvote button
        downvote_button.click()
        return

    def comment(self, comment_str):
        # Wait for the <shreddit-post> element to be present
        add_comment_sec = self.wait.until(
            EC.presence_of_element_located(self.locator.ADD_COMMENT_SEC)
        )

        # faceplate_tracker = add_comment_sec.find_element(
        #     By.XPATH, './/faceplate-tracker[@source="comment_composer"]'
        # )

        # show_edit_sec_btn = faceplate_tracker.find_element(By.TAG_NAME, "button")

        # show_edit_sec_btn.click()

        # comment_edit_area = self.wait.until(
        #     EC.presence_of_element_located(self.locator.COMMENT_EDIT_AREA)
        # )
        # enter_edit_sec = comment_edit_area.find_element(By.XPATH, '//div[@name="body"]')
        # enter_edit_sec_p = enter_edit_sec.find_element(By.TAG_NAME, "p")
        # enter_edit_sec_p.click()
        # enter_edit_sec_p.send_keys(comment_str)

        # submit_btn = comment_edit_area.find_element(
        #     By.XPATH, '//button[@type="submit"]'
        # )
        # submit_btn.click()

        faceplate_tracker = self.wait.until(
            lambda driver: add_comment_sec.find_element(
                By.XPATH, './/faceplate-tracker[@source="comment_composer"]'
            )
        )
        show_edit_sec_btn = self.wait.until(
            lambda driver: faceplate_tracker.find_element(By.TAG_NAME, "button")
        )
        show_edit_sec_btn.click()
        comment_edit_area = self.wait.until(
            EC.presence_of_element_located(self.locator.COMMENT_EDIT_AREA)
        )
        enter_edit_sec = self.wait.until(
            lambda driver: comment_edit_area.find_element(
                By.XPATH, '//div[@name="body"]'
            )
        )
        enter_edit_sec_p = self.wait.until(
            lambda driver: enter_edit_sec.find_element(By.TAG_NAME, "p")
        )
        enter_edit_sec_p.click()
        enter_edit_sec_p.send_keys(comment_str)
        submit_btn = self.wait.until(
            lambda driver: comment_edit_area.find_element(
                By.XPATH, '//button[@type="submit"]'
            )
        )
        submit_btn.click()
