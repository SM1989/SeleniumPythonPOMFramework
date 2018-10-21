import moment
import allure
import json

URL = "https://opensource-demo.orangehrmlive.com/"
USERNAME = "Admin"
PASSWORD = "admin123"


def screenshot(self):
    print("Inside Screenshot Def")
    x = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
    y = "screenshot_" + x
    print("Captured the Screenshot named::", y)
    self.driver.get_screenshot_as_file("C:/Users/saurmukh/PycharmProjects/AutomationFrameword/screenshots/" +y+ ".PNG")

    #Below line works fine with allure adopter
    # allure.MASTER_HELPER.attach(name=y, contents=self.driver.get_screenshot_as_png(),
    #                             type=allure.MASTER_HELPER.attach_type.PNG)

    #Below line works fine with allure-pytest
    allure.attach(self.driver.get_screenshot_as_png(),name=y,attachment_type=allure.attachment_type.PNG)

def open_json_file(filepath):
    with open(filepath) as jsonFile:
        jsonData = json.load(jsonFile)
        return jsonData