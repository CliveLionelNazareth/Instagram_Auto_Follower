from selenium import webdriver
import selenium.common.exceptions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from pprint import pprint
import time
import os
import login_manager
import follow_the_follower

# Note: You may be flagged for botting if you use this too often
# Link to the requested account whose followers will be followed
INSTAGRAM_ACCOUNT_LINK = "https://www.instagram.com/antics_of_scarborough_man/"

# Login using the stored credential info and return the driver
Login_Manager = login_manager.Login_Manager()
driver = Login_Manager.login()
# Pass the driver to the Follow_The_Follower class
Follow_The_Follower = follow_the_follower.Follow_The_Follower(driver, INSTAGRAM_ACCOUNT_LINK)
Follow_The_Follower.follow()
