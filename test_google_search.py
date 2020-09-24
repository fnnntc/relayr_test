from selenium import webdriver
import pytest
from locators import googleMainPageLocators
import base_page
from main_page import MainPage
import allure


@allure.step("Test for searching text")
def test_search(driver):
    p = MainPage(driver)
    p.accept_GDPR()
    p.search("Anton Mishin")


"""...."""