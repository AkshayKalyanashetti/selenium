from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def test_logindemo(un, pw, expected_result):
    driver = webdriver.Chrome("C:\\Users\\Akshay\\Downloads\\chrome\\chromedriver")
    driver.maximize_window()
    driver.get("https://demo.actitime.com")
    driver.find_element_by_id("username").send_keys(un)
    driver.find_element_by_name("pwd").send_keys(pw)
    driver.find_element_by_id("loginButton").click()

    wait = WebDriverWait(driver, 10)
    status = False

    try:
        status = wait.until(ec.title_is(exipected_result))
    except TimeoutException:
        status = False
    driver.quit()

    return status