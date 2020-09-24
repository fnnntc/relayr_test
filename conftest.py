import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver(request):
    browser= webdriver.Chrome(executable_path="./chromedriver.exe")
    yield browser
    #driver.maximize_window()
    browser.quit()