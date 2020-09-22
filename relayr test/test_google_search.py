from selenium import webdriver
import pytest
from locators import googleMainPageLocators
import base_page
import main_page
import allure

@allure.step("Test setup")
def test_setup():
    global driver
    driver= webdriver.Chrome(executable_path=".\chromedriver.exe")
    #driver.maximize_window()

@allure.step("Test for accpeting the GDPR")
def test_accept_GDPR():
    p = main_page.MainPage(driver)
    p.driver.switch_to.frame(0)
    p.accept_GDPR()


@allure.step("Test for searching text")
def test_search():
    p = main_page.MainPage(driver)
    p.search("Anton Mishin")

@allure.step("Test teardown")
def test_teardown():
    driver.close()
    driver.quit()


"""t=GoogleSearch()
t.test_setup()
t.test_accept_GDPR()
t.test_search("qwe")
t.test_teardown()"""