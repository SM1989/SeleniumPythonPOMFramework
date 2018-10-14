import moment
import allure

URL = "https://opensource-demo.orangehrmlive.com/"
USERNAME = "Admin"
PASSWORD = "admin123"


def screenshot(self):
    print("Inside Screenshot Def")
    x = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
    y = "screenshot_" + x
    print("Captured the Screenshot named::", y)
    self.driver.get_screenshot_as_file("C:/Users/saurmukh/PycharmProjects/AutomationFrameword/screenshots/" +y+ ".PNG")
    allure.MASTER_HELPER.attach(name=y, contents=self.driver.get_screenshot_as_png(),
                                type=allure.MASTER_HELPER.attach_type.PNG)