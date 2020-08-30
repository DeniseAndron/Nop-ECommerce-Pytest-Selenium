import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByName_005:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  #Logger

    customerFirstName = ReadConfig.getSearchFirstName()
    customerLastName = ReadConfig.getSearchLastName()
    customerFullName = ReadConfig.getSearchFullName()


    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setUp):
        self.logger.info("***** SearchCustomerByName_005 ******")
        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** Login Successful ***")

        self.logger.info(" *** Starting Search Customer by Name ***")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("*** searching customer by Name")
        searchCust = SearchCustomer(self.driver)
        searchCust.setFirstName(self.customerFirstName)
        searchCust.setLastName(self.customerLastName)
        searchCust.clickSearch()
        time.sleep(3)
        status = searchCust.searchCustomerByName(self.customerFullName)
        assert True == status
        self.logger.info(" ***** TC_SearchCustomerByName_005 Finished ****")

        self.driver.close()