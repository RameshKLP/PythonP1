from selenium.webdriver.common.by import By
from Locators.locators import locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, locators.username_textbox_id).clear()
        self.driver.find_element(By.ID, locators.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, locators.password_testbox_id).clear()
        self.driver.find_element(By.ID, locators.password_testbox_id).send_keys(password)

    def clickonLogin(self):
        self.driver.find_element(By.ID, locators.login_button_id).click()

    def check_invalid_username_message(self):
        msg=self.driver.find_element(By.XPATH, locators.invalid_login_message_xpath).text
        return msg




