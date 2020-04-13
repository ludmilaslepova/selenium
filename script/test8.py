from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num_1 = int(browser.find_element_by_id("num1").text)
    num_2 = int(browser.find_element_by_id("num2").text)
    sum_num = num_1 + num_2

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum_num))

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()