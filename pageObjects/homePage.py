from selenium.webdriver.common.by import By

from Locators.locators import locators

class HomePage():

    def __init__(self, driver):
        self.driver= driver



    def click_welcome(self):
        self.driver.find_element(By.ID, locators.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, locators.logout_link_linktext).click()



