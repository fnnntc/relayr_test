from selenium.webdriver.common.by import By

class googleMainPageLocators():
    BASE_URL = "https://google.com/"
    AGREE_BUTTON = (By.ID, "introAgreeButton")
    MAIN_LOGO = (By.XPATH, "//img[@alt='Google']")
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_LOGO = (By.CLASS_NAME, "hsuHs")
    MIC = (By.CLASS_NAME, "hpuQDe")
    SEARCH_BUTTON = (By.XPATH, "//div[@class='FPdoLc tfB0Bf']//input[@name='btnK']")
    LUCKY_BUTTON = (By.XPATH, "//div[@class='FPdoLc tfB0Bf']//input[@name='btnI']")
    SEARCH_RESULT_STATS = (By.ID, "result-stats")
    