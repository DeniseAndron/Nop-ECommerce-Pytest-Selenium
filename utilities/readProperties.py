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
        customerPassword = config.get('add customer info', 'customerPassword')

    @staticmethod
    def getCustomerRoles():
        customerRoles = config.get('add customer info', 'customerRoles')

    @staticmethod
    def getVendor():
        vendor = config.get('add customer info', 'vendor')

    @staticmethod
    def getGender():
        gender = config.get('add customer info', 'gender')

    @staticmethod
    def getFirstName():
        firstname = config.get('add customer info', 'firstname')

    @staticmethod
    def getLastName():
        lastname = config.get('add customer info', 'lastname')

    @staticmethod
    def getDateOfBirth():
        getdob = config.get('add customer info', 'setdob')

    @staticmethod
    def getCompany():
        company = config.get('add customer info', 'company')

    @staticmethod
    def getAdminContent():
        adminContent = config.get('add customer info', 'adminContent')
