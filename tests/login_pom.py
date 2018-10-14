from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.constants import *

class Login():
    driver = webdriver.Chrome(executable_path= "../drivers/chromedriver.exe")
    login = LoginPage(driver)
    home = HomePage(driver)
    login.test_setup()
    login.test_login(USERNAME, PASSWORD)
    home.test_navigation("Admin")
    home.test_navigation("PIM")
    home.test_navigation("Leave")
    home.test_navigation("Time")
    home.test_navigation("Performance")
    home.test_navigation("Dashboard")
    home.test_navigation("Directory")
    home.test_logout()
    home.test_quit()