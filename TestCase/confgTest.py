import pytest
from selenium import webdriver


# fixture will run at the begingig of the test
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
    return driver


def pytest_addoption(parser): # this will get value from cli hook
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


# PYTEST HTML REPORTS
# we will diplay what all things we want to display
def pytest_confg(config):
    config._metadata['Project name'] = 'nop commerce'
    config._metadata['Module name'] = 'Customer'
    config._metadata['Tester'] = 'Anjali'

# it is hook for delete/modify environment  info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)


