import moment
import allure
import json

# x = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
# print(x)
# y = "screenshot_" + x
# print(y)
# print("Made some changes to Push in GIT")
# #
#
# def screenshot(self):
#     print("Inside Screenshot Def")
#     x = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
#     print(x)
#     y = "screenshot_" + x
#     print(y)
#     self.driver.get_screenshot_as_file("C:/Users/saurmukh/PycharmProjects/AutomationFrameword/screenshots/" +y+ ".PNG")
#     allure.MASTER_HELPER.attach(name=y, contents=self.driver.get_screenshot_as_png(),
#                                 type=allure.MASTER_HELPER.attach_type.PNG)

with open("C:/Users/saurmukh/PycharmProjects/AutomationFrameword/data/user_details.json") as jsonFile:
    jsonData = json.load(jsonFile)
    print(jsonData['username'])
