#reads the common data from the config.ini

import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    #add customer page

    @staticmethod
    def getCustomerPassword():
        customerPassword = config.get('customer info', 'customerPassword')
        return customerPassword

    @staticmethod
    def getCustomerRoles():
        customerRoles = config.get('customer info', 'customerRoles')
        return customerRoles

    @staticmethod
    def getVendor():
        vendor = config.get('customer info', 'vendor')
        return vendor

    @staticmethod
    def getGender():
        gender = config.get('customer info', 'gender')
        return gender

    @staticmethod
    def getFirstName():
        firstname = config.get('customer info', 'firstname')
        return firstname

    @staticmethod
    def getLastName():
        lastname = config.get('customer info', 'lastname')
        return lastname

    @staticmethod
    def getDateOfBirth():
        getdob = config.get('customer info', 'setdob')
        return getdob

    @staticmethod
    def getCompany():
        company = config.get('customer info', 'company')
        return company

    @staticmethod
    def getAdminContent():
        adminContent = config.get('customer info', 'adminContent')
        return adminContent

    @staticmethod
    def getSearchEmail():
        custEmail = config.get('search by email', 'custemail')
        return custEmail

    @staticmethod
    def getSearchFirstName():
        custName = config.get('search by name', 'custfirstname')
        return custName

    @staticmethod
    def getSearchLastName():
        custName = config.get('search by name', 'custlastname')
        return custName

    @staticmethod
    def getSearchFullName():
        custName = config.get('search by name', 'custFullName')
        return custName
