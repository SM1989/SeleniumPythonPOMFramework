from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.constants import *
import pytest
import allure

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(URL)
        login = LoginPage(driver)
        login.test_login(USERNAME, PASSWORD)

    def test_homepage_basic(self):
        driver = self.driver
        global home
        home = HomePage(driver)
        home.test_navigation("Admin")
        home.test_navigation("PIM")
        home.test_navigation("Leave")
        home.test_navigation("Time")
        home.test_navigation("Performance")
        home.test_navigation("Dashboard")
        home.test_navigation("Directory")

    def test_logout(self):
        # home = HomePage(driver)
        home.test_logout()