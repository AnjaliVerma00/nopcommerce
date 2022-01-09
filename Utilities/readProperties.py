import configparser
import parser
import iniconfig

#this method will use to read the ini file
config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.init')


class ReadConfig:
    #create number of method for defined in ini file
    # creating method as static method so we dnt have to create an instance
    @staticmethod
    def geturl():
        # get url from ini file using config instannce
        url = config.get('common info','baseurl')
        return url

    @staticmethod
    def getusername():
        username = config.get('common info','username')
        return username

    @staticmethod
    def getpassword():
        passwrd = config.get('common info','password')
        return passwrd