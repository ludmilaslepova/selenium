import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_buy_button(browser):
    time.sleep(5)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[type='submit']"))) 