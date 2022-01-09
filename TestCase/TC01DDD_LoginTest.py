import pytest
from selenium import webdriver
from PageObject.login import Login
from Utilities.readProperties import ReadConfig
from Utilities.customerLogger import LogGen
from Utilities import XLUtils
import time


class TC01DDD_LoginTest:
    # create global variable
    baseurl = ReadConfig.geturl()
    path = ".//TestData/Data.xlsx"

    # create a variable that will contain return object
    # this is class variable
    logger = LogGen.loggen()

    def test_logind(self):
        self.logger.info("*********test_loginDDD***********")
        self.driver = webdriver.Chrome(executable_path ='C:\Drivers\chromedriver_win32\chromedriver.exe')
        self.driver.get(self.baseurl)
        # as Login class does not have static method we need to initialize with self as it is related to class
        # Login class has constructor that need driver so while calling class we need to pass driver
        self.lp = Login(self.driver)
        self.rows = XLUtils.getrowcount(self.path, 'Sheet1')
        ststus = []
        for r in range(2, self.rows+1):
            self.user = XLUtils.readdata(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readdata(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readdata(self.path, 'Sheet1', r, 3)
            self.lp.setusername(self.user)
            self.lp.setpaswrd(self.password)
            self.lp.loginbttn()
            time.sleep(5)
            acttiele = self.driver.title
            exptitle = 'Dashboard / nopCommerce administration'
# sending expected data also in testdat and if all 3 contion pass then TC pass
            if acttiele == exptitle:
                if self.exp == 'Pass':
                    self.logger.info("**passed")
                    self.lp.logoutbtn()
                    ststus.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("**failed")
                    self.lp.logoutbtn()
                    ststus.append("fail")
            elif acttiele != exptitle:
                if self.exp == 'Pass':
                    self.logger.info("**failed")
                    self.lp.logoutbtn()
                    ststus.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**Pass")
                    self.lp.logoutbtn()
                    ststus.append("Pass")
            if "Fail" not in ststus:
                self.logger.info("login TC passed")
                self.driver.close()
                assert True
            else:
                self.logger.info("login TC failed")
                assert False