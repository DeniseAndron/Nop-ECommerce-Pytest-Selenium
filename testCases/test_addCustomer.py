import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    customerPassword = ReadConfig.getCustomerPassword()
    customerRoles = ReadConfig.getCustomerRoles()
    vendor = ReadConfig.getVendor()
    gender = ReadConfig.getGender()
    firstName = ReadConfig.getFirstName()
    lastName = ReadConfig.getLastName()
    dob = ReadConfig.getDateOfBirth()
    company = ReadConfig.getCompany()
    adminContent = ReadConfig.getAdminContent()


    logger = LogGen.loggen()


    def test_addCustomer(self, setUp):
        self.logger.info("***** Test_003_AddCustomer****")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** Login succesful ****")

        self.logger.info("**** Starting Add Customer Test***")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()



        self.logger.info("*** Providing customer info ***")

        self.email = random_generator() + "@gmail.com"
        time.sleep(2)
        self.addcust.setEmail(self.email)
        self.addcust.setCustomerPassword(self.customerPassword)
        self.addcust.setCustomerRoles(self.customerRoles)
        self.addcust.setManagerOfVendor(self.vendor)
        self.addcust.setGender(self.gender)
        self.addcust.setFirstName(self.firstName)
        self.addcust.setLastName(self.lastName)
        self.addcust.setDob(self.dob)
        self.addcust.setCompanyName(self.company)
        self.addcust.setAdminContent(self.adminContent)
        self.addcust.clickOnSave()

        self.logger.info("**** Saving customer info *****")

        self.logger.info("*** Add customer validation started ****")

        self.msg = self.driver.find_element_by_tag_name("body").text



        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("***** Add customer Test Passed ****")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("*** Add customer Test Failed ***")
            assert True == False

        self.driver.close()
        self.logger.info(" **** Ending Home Page Title Test ****")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))