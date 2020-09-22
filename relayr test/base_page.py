from locators import googleMainPageLocators

class BasePage(object):

    IMP_WAIT = 5

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(self.IMP_WAIT)
        driver.get(googleMainPageLocators.BASE_URL)

    def check_if_displayed(self,locator):
        try:
            isDisplayed = locator.is_displayed()
        except:
            isDisplayed = False
            raise AssertionError('Element {} is not displayed'.format(locator))
        assert isDisplayed == True

    def check_not_displayed(self,locator):
        try:
            isDisplayed = locator.is_displayed()
        except:
            isDisplayed = False
        assert isDisplayed == False, "Element {} is displayed".format(locator)
