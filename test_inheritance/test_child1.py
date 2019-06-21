from test_inheritance.test_base import Test_Demo
from selenium import webdriver


class Test_Demo1:


     def abc(self):
         driver = webdriver.Chrome('C:\\Users\\Akshay\\Downloads\\chrome\\chromedriver')driver.find_element_by_xpath('//*[@id="topnav"]/tbody/tr[1]/td[3]/a/div[1]').click()
         print("executing")

dd = Test_Demo

#dd1 = Test_Demo1().abc()





