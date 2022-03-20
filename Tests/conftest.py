from selenium import webdriver

import pytest

from Config.Config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def setup(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
