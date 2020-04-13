from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    tr = browser.find_element_by_id("treasure")

    y = calc(tr.get_attribute("valuex"))
    
    field = browser.find_element_by_id("answer")
    field.send_keys(y)

    option_1 = browser.find_element_by_id("robotCheckbox")
    option_1.click()

    option_2 = browser.find_element_by_id("robotsRule")
    option_2.click()

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

    time.sleep(5)

finally:
    time.sleep(5)
    browser.quit()
