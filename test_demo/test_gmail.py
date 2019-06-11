import pytest
from selenium import webdriver
def test_gmail():

    driver = webdriver.Chrome("C:\\Users\\Akshay\\Downloads\\chrome\\chromedriver")
    driver.get('https://google.com')
    driver.get('https://gmail.com')
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]/ul[1]/li[2]/a").click()
   # driver.find_element_by_name('identifier').send_keys('aksh')