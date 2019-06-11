import pytest
from selenium import webdriver
def test_gmail():

    driver = webdriver.Chrome("C:\\Users\\Akshay\\Downloads\\chrome\\chromedriver")
    driver.get('https://google.com')
    driver.get('https://demo.actitime.com')
