import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser(request):
    #global driver
    browser= webdriver.Chrome(executable_path="D:/Programming/relayr test/chromedriver.exe")
    yield browser
    #driver.maximize_window()
