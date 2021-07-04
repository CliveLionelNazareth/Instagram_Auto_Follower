import time

from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os

# Set the Username and password as environment variables
INSTAGRAM_USERNAME = os.environ["INSTAGRAM_USERNAME"]
INSTAGRAM_PASSWORD = os.environ["INSTAGRAM_PASSWORD"]


class Login_Manager:
    def __init__(self):
        # Sets up chromedriver, username, password and mentioned link for later use
        chrome_driver_path = "C:\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.username = INSTAGRAM_USERNAME
        self.password = INSTAGRAM_PASSWORD

    def login(self):
        # Enter the Instagram login page
        self.driver.get('https://www.instagram.com/accounts/login/')
        # Pause to let the webpage load
        time.sleep(10)
        # Find the elements to enter the username and password and enter the username and password
        user_name_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        password_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        user_name_field.send_keys(self.username)
        password_field.send_keys(self.password)
        # Click the login button
        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/button')
        login_button.click()
        # Pause to let the webpage load
        time.sleep(10)
        # Returns the driver for use in the Follow_The_Follower class
        return self.driver
