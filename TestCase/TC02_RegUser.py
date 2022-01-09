import pytest
from selenium import webdriver
from PageObject.login import Login
from PageObject.Addcutomer import register
from Utilities.readProperties import ReadConfig
from Utilities.customerLogger import LogGen


class Test_LoginTest:
    # create global variable
    baseurl = ReadConfig.geturl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    # create a variable that will contain return object
    #this is class variable
    logger =  LogGen.loggen()

    def test_addcustomer(self):
        self.logger.info("*********test_login***********")
        self.driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
        self.driver.get(self.baseurl)
        # as Login class does not have static method we need to initialize with self as it is related to class
        # Login class has constructor that need driver so while calling class we need to pass driver
        self.lp = Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpaswrd(self.password)
        self.lp.loginbttn()
        self.logger.info("*********test_loginsuccessfull***********")
        self.addcus = register(self.driver)
        self.addcus.clickonCustomerMenu()
        self.addcus.custmr()
        self.addcus.addnew()
        self.addcus.enterEmail('abhju12@gmail.com')
        self.addcus.enterPass('Pass123')
        self.addcus.firstname('Ana')
        self.addcus.lastname('pa')
        self.addcus.gender()
        self.addcus.setdob('12/12/2021')
        self.addcus.save()
        self.logger.info("*********regsiter successfully***********")