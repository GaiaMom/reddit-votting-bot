import pandas as pd
import logging
import time

from .ghost_logger import GhostLogger

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.article_page import ArticlePage

class BotManager:
    def __init__(self, file_path, verbose: bool = False):
        self.logger = GhostLogger
        if verbose:
            self.verbose = True
            # configure logging
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.INFO)
            self.logger.addHandler(logging.StreamHandler())
            formatter = logging.Formatter(
                "\033[93m[INFO]\033[0m %(asctime)s \033[95m%(message)s\033[0m"
            )
            self.logger.handlers[0].setFormatter(formatter)

        self.file_path = file_path
        self.data = None
        self.expected_headers = [
            "serial_number",
            "link",
            "username",
            "pass",
            "mail",
            "mail_pass",
            "upvote",
            "downvote",
            "comment",
        ]

    def read_first_sheet(self):
        # Read the first sheet of the Excel file
        try:
            df = pd.read_excel(self.file_path, sheet_name=0)
            self.validate_table(df)
            self.process_data(df)
            self.data = df.to_dict(orient="records")
        except Exception as e:
            print(f"Error reading the Excel file: {e}")

    def validate_table(self, df):
        # Check if the DataFrame matches the expected headers
        if list(df.columns) != self.expected_headers:
            raise ValueError("Table headers do not match the expected format.")

        # Check data types and defaults
        for index, row in df.iterrows():
            # Check serial_number is int
            if (
                not isinstance(row["serial_number"], (int, float))
                or not row["serial_number"].is_integer()
            ):
                raise ValueError(f"Row {index+1}: serial_number must be an integer.")

            # Validate upvote and downvote logic
            upvote = row["upvote"].lower()
            downvote = row["downvote"].lower()
            if upvote not in ["yes", "no"] or downvote not in ["yes", "no"]:
                raise ValueError(
                    f"Row {index+1}: upvote and downvote must be 'yes' or 'no'."
                )

            # Set defaults if not provided
            if upvote == "yes" and downvote == "yes":
                df.at[index, "downvote"] = "no"

            if upvote not in ["yes", "no"]:
                df.at[index, "upvote"] = "no"
            if downvote not in ["yes", "no"]:
                df.at[index, "downvote"] = "no"

    def process_data(self, df):
        # Any additional processing can go here
        pass

    def vote_actions(self):
        base_page = BasePage(self.driver, self.wait)
        prev_link = ""
        count = 0
        success_list = []
        fail_list = []
        last_success = True
        
        s_time = time.time()
        for action in self.data:
            if (count >= 5):
                break
            try:
                print(f"Username: {action["username"]}, Password: {action["pass"]} is logging ..... ")
                
                page_loading_s_time = time.time()
                if (prev_link != action["link"] or (not last_success)):
                    base_page.go_to_page(action["link"])
                prev_link = action["link"]
                print(f"1: {(time.time() - page_loading_s_time): .2f}s ")
                
                page_loading_s_time = time.time()
                
                login_page = LoginPage(self.driver, self.wait)
                login_page.login(action["username"], action["pass"])
                
                time.sleep(10)
                
                article_page = ArticlePage(self.driver, self.wait)
                if (action['upvote'] == 'yes'):
                    article_page.upvote()
                else:
                    article_page.downvote()
                    
                time.sleep(10)
                article_page.comment(action["comment"])
                time.sleep(10)
                login_page.logout()
                time.sleep(10)
                
                last_success = True
                success_list.append(action)
                print(f"2: {(time.time() - page_loading_s_time): .2f}s ")
                
            except Exception as e:
                self.logger.error(f"An error occurred: {e}")
                print(f"An error occurred: {e}")
                last_success = False
                fail_list.append(action)
                
            finally:
                count = count + 1
                
        print(f"Total Time: {(time.time() - s_time): .2f}s ")
                
        print(f"\nSuccess : {len(success_list)}, Fail : {len(fail_list)}")
        print(f"\nSuccess List\n{success_list}")
        print(f"\nFail List\n{fail_list}")
        
    def start_selenium(self):
        options = webdriver.ChromeOptions()
    
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        # # options.add_argument('--window-size=1920,1080')
        # options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-features=IsolateOrigins,site-per-process")
        options.add_argument("--disable-extensions")
        
        # Disable image loading
        prefs = {
            "profile.managed_default_content_settings.images": 2  # 2 means block images
        }
        options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()), options=options)
        self.driver.execute_cdp_cmd("Network.setBlockedURLs", {"urls": ["*.mp4", "*.webm", "*.ogg", "*.mov"]})

        self.wait = WebDriverWait(self.driver, 30)

    def close_selenium(self):
        if self.driver:
            self.driver.quit()
