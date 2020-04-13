from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    field = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button_first = browser.find_element(By.TAG_NAME, "button")
    button_first.click()

    y = calc(browser.find_element_by_id("input_value").text)

    field = browser.find_element_by_tag_name("input")
    field.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text

    print(alert_text)

finally:
    #time.sleep(3)
    browser.quit()