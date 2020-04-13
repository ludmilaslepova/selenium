from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    answ = calc(browser.find_element_by_id("input_value").text)

    browser.execute_script("window.scrollBy(0, 100);")

    field = browser.find_element_by_id("answer")
    field.send_keys(answ)

    option_1 = browser.find_element_by_id("robotCheckbox")
    option_1.click()

    option_2 = browser.find_element_by_id("robotsRule")
    option_2.click()

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(8)
    browser.quit()

