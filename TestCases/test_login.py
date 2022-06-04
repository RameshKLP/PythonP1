import time
import pytest

from pageObjects.homePage import HomePage
from pageObjects.loginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_Login_test():
    logger = LogGen.loggen()
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_valid(self, setup):
        self.logger.info("*************** Test_001_Login Started*****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        login = LoginPage(self.driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.clickonLogin()
        act_title = self.driver.title
        print("Title= ", act_title)
        if act_title == "OrangeHRM":
            self.logger.info("****Login test passed ****")
            self.logger.info("*************** Test_001_Login ended*****************")
            homepage = HomePage(self.driver)
            homepage.click_welcome()
            homepage.click_logout()
            assert True
        else:
            time.sleep(3)
            assert False
        time.sleep(3)

    @pytest.mark.regression
    def test_login_invalid(self, setup):
        self.driver = setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        login = LoginPage(self.driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.clickonLogin()
        message = login.check_invalid_username_message()
        print(message)
        if message == "Invalid credentials":
            self.logger.info("**** Home page title test passed ****")
            time.sleep(3)
            assert True
        else:
            time.sleep(3)
            assert False
