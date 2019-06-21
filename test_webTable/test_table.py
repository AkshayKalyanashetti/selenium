import pytest
from selenium import webdriver

class Test_demo:
    def test_table(self):
        self.driver = webdriver.Chrome("C:\\Users\\Akshay\\Downloads\\chrome\\chromedriver")
        self.driver.get("file:///C:/Users/Akshay/Documents/demo.html")
        self.driver.implicitly_wait(30)
        ele = self.driver.find_element_by_xpath("//*[@id='123']/tbody/tr[1]/td[1]")
        print(ele.text)



