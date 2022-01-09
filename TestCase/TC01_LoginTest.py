import pytest
from selenium import webdriver
from PageObject.login import Login
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

    # create method test to check the title of the page
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self):
        self.logger.info("*********test_homePageTitle***********")
        self.logger.info("*********verify title***********")
        self.driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
        self.driver.get(self.baseurl)
        actl = self.driver.title
        if actl == 'Admin area demo':
            assert True
            self.driver.close()
            self.logger.error("****************home page title failed****")
        else:
            self.driver.save_screenshot('.\\Screenshot\\' + 'img1.png')
            self.driver.close()
            assert False

    def test_login(self):
        self.logger.info("*********test_login***********")
        self.driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
        self.driver.get(self.baseurl)
        # as Login class does not have static method we need to initialize with self as it is related to class
        # Login class has constructor that need driver so while calling class we need to pass driver
        self.lp = Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpaswrd(self.password)
        self.lp.loginbttn()
        title = self.driver.title
        if title == 'Dashboard / nopCommerce administration':
            assert True
            self.driver.close()
            self.logger.info("****************home page title passed****")
        else:
            self.driver.save_screenshot('.\\Screenshot\\' + 'img2.png')
            self.driver.close()
            assert False
