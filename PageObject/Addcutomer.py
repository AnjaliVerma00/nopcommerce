from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class register():
    custommenu = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    custmr = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    addnew = "//a[@class ='btn btn-primary']"
    emailID = "Email"
    PasswrdID = "Password"
    FnameID = "FirstName"
    LnameID = "LastName"
    gendrmaleID = 'Gender_Male'
    gendrFemaleID = "Gender_Female"
    DOBID = "DateOfBirth"
    SAVENAME = "save"

    def __init__(self,driver):
        self.driver = driver

    def clickonCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.custommenu).click()

    def selectCustomer(self):
        self.driver.find_element(By.XPATH,self.custmr).click()

    def clickAddnew(self):
        self.driver.find_element(By.XPATH,self.addnew).click()

    def enterEmail(self,email):
         self.driver.find_element(By.ID,self.emailID).send_keys(email)

    def enterPass(self, Passwrd):
        self.driver.find_element(By.ID, self.PasswrdID).send_keys(Passwrd)

    def firstname(self, Name):
        self.driver.find_element(By.ID, self.FnameID).send_keys(Name)

    def lastname(self, Lname):
        self.driver.find_element(By.ID, self.LnameID).send_keys(Lname)

    def gender(self):
        self.driver.find_element(By.ID,self.gendrFemaleID).click()

    def setdob(self, date):
        self.driver.find_element(By.ID, self.DOBID).send_keys(date)

    def save(self,dob):
        self.driver.find_element(By.NAME,self.setdob).send_keys(dob)


