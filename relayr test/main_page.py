from locators import googleMainPageLocators
from base_page import BasePage

class MainPage(BasePage):
    
    def accept_GDPR(self):
        btn = self.driver.find_element(*googleMainPageLocators.AGREE_BUTTON)
        btn.click()
        self.check_not_displayed(btn)

    def search(self,query):
        search_input = self.driver.find_element(*googleMainPageLocators.SEARCH_INPUT)
        search_btn = self.driver.find_element(*googleMainPageLocators.SEARCH_BUTTON)
        search_input.send_keys(query)
        search_btn.click()
        results = self.driver.find_element(*googleMainPageLocators.SEARCH_RESULT_STATS)
        self.check_if_displayed(results)
