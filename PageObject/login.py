import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Login():
    usernameid = "Email"
    passwrdid = "Password"
    loginxpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    logoutlink= "Logout"

# create a class constructor having driver and can be access throughout the class
    def __init__(self,driver):
        self.driver = driver

# send username as paramter where which user we want to login
# to access the global locator need to use self.
    def setusername(self, username):
        self.driver.find_element(By.ID, self.usernameid).clear()
        self.driver.find_element(By.ID, self.usernameid).send_keys(username)

    def setpaswrd(self, passwrd):
        self.driver.find_element(By.ID, self.passwrdid).clear()
        self.driver.find_element(By.ID, self.passwrdid).send_keys(passwrd)

    def loginbttn(self):
        self.driver.find_element(By.XPATH,self.loginxpath).click()

    def logoutbtn(self):
        self.driver.find_element(By.LINK_TEXT, self.logoutlink).click()



