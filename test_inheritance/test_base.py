import pytest
from selenium import webdriver
class Test_Demo:
    driver = webdriver.Chrome("C:\\Users\\Akshay\\Downloads\\chrome\\chromedriver")

    def test_actitime(self):
        global driver
        driver = webdriver.Chrome("C:\\Users\\Akshay\\Downloads\\chrome\\chromedriver")
        driver.get("https://google.com")
        driver.get("https://demo.actitime.com")
        driver.maximize_window()
        abc = driver.title
        print(abc)
        assert(abc == "actiTIME - Login", 'NOt matching so failed')
        #assertTrue(abc == "actiTIME - Login")

    def test_username(self):
        driver.find_element_by_id('username').send_keys('admin')
        driver.find_element_by_name('pwd').send_keys('manager')
        driver.find_element_by_xpath('//*[@id="loginButton"]/div').click()
        x = driver.title
        print(x)
        print('complted')

