from pages.xpaths import *
from utils.constants import *
from pages.home_page import *
import time
import json

class Admin():

    jsonfile = open_json_file("C:/Users/saurmukh/PycharmProjects/AutomationFrameword/data/user_details.json")
    username = jsonfile['username']
    print(username)

    def __init__(self, driver):
        self.driver = driver

    def search_user(self):
        home = HomePage(self.driver)
        home.test_navigation("Admin")
        self.driver.find_element_by_xpath(XPATH_ADMINPAGE_USERNAME).clear()
        self.driver.find_element_by_xpath(XPATH_ADMINPAGE_USERNAME).send_keys(self.username)
        time.sleep(2)
        self.driver.find_element_by_xpath(XPATH_ADMINPAGE_SEARCHBUTTON).click()
        time.sleep(5)
        try:
            print("Inside Try Block")
            screenshot(self)
            self.driver.find_elements_by_xpath(XPATH_ADMINPAGE_ROWS)
            print("Found the Rows")
            # assert 1 == 0
        except:
            print("Inside Except Block")
            screenshot(self)
            assert 1 == 0