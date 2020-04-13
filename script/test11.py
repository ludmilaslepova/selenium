from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_blue = browser.find_element_by_tag_name("button")
    button_blue.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    y = calc(browser.find_element_by_id("input_value").text)

    field = browser.find_element_by_tag_name("input")
    field.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(7)
    browser.quit()