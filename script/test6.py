from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    y = calc(browser.find_element_by_id("input_value").text)
    field = browser.find_element_by_id("answer")
    field.send_keys(y)

    option_1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option_1.click()

    option_2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option_2.click()

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

    time.sleep(5)

finally:
    time.sleep(5)
    browser.quit()
