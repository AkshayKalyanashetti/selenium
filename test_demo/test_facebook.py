import pytest
import pytest_html

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

def test_fb():
    driver = webdriver.Chrome("C:\\Users\\Akshay\\Downloads\\chrome\\chromedriver")
    driver.get('https://google.com')
    driver.get('https://facebook.com')
    driver.implicitly_wait(30)
    driver.find_element_by_name('firstname').send_keys('dhoni')
    driver.find_element_by_name('lastname').send_keys('sing')
    driver.find_element_by_xpath("//input[contains(@id, 'u_')]").send_keys('8971497419')
    driver.find_element_by_name('reg_passwd__').send_keys('Money@123')
    print(Select(driver.find_element_by_name('birthday_day')).is_multiple())
    Select(driver.find_element_by_name('birthday_day')).select_by_value('17')
    Select(driver.find_element_by_name('birthday_month')).select_by_value('7')
    Select(driver.find_element_by_name('birthday_year')).select_by_visible_text('1995')
    time.sleep(1)

   # driver.find_element_by_id('u_0_6').click()