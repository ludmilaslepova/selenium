from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        if element.get_attribute("type") == "text":
            element.send_keys("smth")
        else:
            continue
        
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    button_1 = browser.find_element_by_id("file")
    button_1.send_keys(file_path)

    button_2 = browser.find_element_by_tag_name("button")
    button_2.click()

finally:
    time.sleep(8)
    browser.quit()