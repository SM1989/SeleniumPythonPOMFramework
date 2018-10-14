from pages.xpaths import *
from utils.constants import *
import time

class HomePage():

    def __init__(self, driver):
        self.driver = driver

    def test_logout(self):
        print("Inside Logout Def")
        self.driver.find_element_by_xpath(XPATH_HOMEPAGE_WELCOME).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)
        self.driver.find_element_by_xpath(XPATH_HOMEPAGE_LOGOUT).click()
        print("Logout Completed")
    def test_navigation(self, menuitem):
        print("Inside Navigation Def")
        self.driver.implicitly_wait(10)
        xpath = XPATH_HOMEPAGE_NAVIGATION + menuitem + "']"
        self.driver.find_element_by_xpath(xpath).click()
        print("Clicked on::", menuitem)
        screenshot(self)


    def test_quit(self):
        self.driver.quit()
        print("Browser Closed")