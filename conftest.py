import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in Your Browser Name e.g chrome, Firefox")

@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver

    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path = 'C:/Users/saurmukh/PycharmProjects/AutomationFrameword/drivers/chromedriver.exe')
    elif browser == "Firefox":
        driver = webdriver.Firefox(executable_path= "C:/Users/saurmukh/PycharmProjects/AutomationFrameword/drivers/geckodriver.exe")

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print('Test Completed')