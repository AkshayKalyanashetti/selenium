import pytest
from selenium import webdriver
class Test_Demo:
    driver = webdriver.Chrome("C:\\Users\\Akshay\\Downloads\\chrome\\chromedriver")

    def test_actitime(self):
        self.driver.get("https://google.com")
        self.driver.get("https://demo.actitime.com")
        self.driver.maximize_window()
        abc = self.driver.title
        print(abc)
        assert(abc == "actiTIME - Login", 'NOt matching so failed')
        #assertTrue(abc == "actiTIME - Login")
        #self.assert abc = "actiTIME - Login"
        #self.assert abc.text == 'actiTIME - Login'

    def test_username(self):
        self.driver.find_element_by_id('username').send_keys('admin')
        self.driver.find_element_by_name('pwd').send_keys('manager')
        self.driver.find_element_by_xpath('//*[@id="loginButton"]/div').click()
        x = self.driver.title
        print(x)