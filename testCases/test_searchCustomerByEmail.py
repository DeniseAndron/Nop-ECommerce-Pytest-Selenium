import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByEmail_004:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  #Logger

    customerEmail = ReadConfig.getSearchEmail()

    def test_searchCustomerByEmail(self, setUp):
        self.logger.info("***** SearchCustomerByEmail_004 ******")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** Login Successful ***")

        self.logger.info(" *** Starting Search Customer by Email ***")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("*** searching customer by Email")
        searchCust = SearchCustomer(self.driver)
        searchCust.setEmail(self.customerEmail)
        searchCust.clickSearch()
        time.sleep(3)
        status = searchCust.searchCustomerByEmail(self.customerEmail)
        assert True == status
        self.logger.info(" ***** TC_SearchCustomerByEmail_004 Finished ****")
