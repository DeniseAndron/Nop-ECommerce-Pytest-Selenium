import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

#run the file pytest -v -s testCases/test_login.py


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

# grouping the testcases
    @pytest.mark.regression
    def test_homePageTitle(self,setUp):
        self.logger.info("****** Test_001_Login ***********")
        self.logger.info("**********Verifying Home Page Title **********")
        self.driver = setUp
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == 'Your store. Login':
            assert True
            self.driver.close()
            self.logger.info("**********Home page title is passed **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("**********Home page title is failed **********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setUp):
        self.logger.info("**********Verify login test**********")

        self.driver = setUp
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #verify the successful login
        act_title = self.driver.title
        if act_title == 'Dashboard / nopCommerce administration':
            assert True
            self.driver.close()
            self.logger.info("**********Login test is passed **********")


        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("**********Login page title is failed **********")

            assert False



