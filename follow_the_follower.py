import time
from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Follow_The_Follower:
    def __init__(self, webdriver, account_link):
        # Using the webdriver enter the requested instagram page
        self.driver = webdriver
        self.driver.get(account_link)
        time.sleep(10) \
            # Find and click the account's Followers button
        follower_button = self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        follower_button.click()
        time.sleep(10)
        self.currently_followed = 0

    def find_currently_visible_followers(self):
        """Returns a list of all current visible followers"""
        return self.driver.find_elements_by_css_selector("li div div button")

    def follow(self):
        # Loop until we run out of Followers
        while True:
            # Scroll down 5 times
            fBody = self.driver.find_element_by_xpath("//div[@class='isgrP']")
            scroll = 0
            while scroll < 5:
                self.driver.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                    fBody)
                time.sleep(2)
                scroll += 1
            # Get the list of currently visible followers
            follower_list = self.find_currently_visible_followers()
            follower_list_len = len(follower_list)
            if follower_list_len == self.currently_followed:
                # Exit if after scrolling there are no new followers
                break
            else:
                # For the initial run, follow all currently visible followers
                # Follow all the new followers generated by scrolling.
                for to_follow_account in range(self.currently_followed, follower_list_len):
                    if follower_list[to_follow_account].text == "Follow":
                        follower_list[to_follow_account].click()
                        time.sleep(1)
                    self.currently_followed += 1
