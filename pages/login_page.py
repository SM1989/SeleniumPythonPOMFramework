from pages.xpaths import *
import allure
from utils.constants import *

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
    def test_setup(self):
        self.driver.get(URL)
        self.driver.maximize_window()
        print("Setup Completed")

    def test_login(self, uername, password):
        print("Inside Login Definition")
        self.driver.find_element_by_xpath(XPATH_LOGINPAGE_USERNAME).clear()
        self.driver.find_element_by_xpath(XPATH_LOGINPAGE_USERNAME).send_keys(uername)
        self.driver.find_element_by_xpath(XPATH_LOGINPAGE_PASSWORD).clear()
        self.driver.find_element_by_xpath(XPATH_LOGINPAGE_PASSWORD).send_keys(password)
        self.driver.find_element_by_xpath(XPATH_LOGINPAGE_LOGIN).click()
        print("Login Completed")
        title = self.driver.title
        print(title)
        try:
            print("Inside Try Block")
            assert title == "Saurabh"
        except:
            print("Inside Except Block")
            screenshot(self)
            print("Done with screenshot")


    def test_quit(self):
        self.driver.quit()
        print("Browser Closed")