import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


@pytest.fixture()
def browser():
    print("\nlaunching your browser")
    browser = webdriver.Chrome()
    yield browser
    print("\nclosing your browser")
    browser.quit()

class TestStepikPages():

    @pytest.mark.parametrize('steps', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_open_links(self, browser, steps):
        link = f"https://stepik.org/lesson/{steps}/step/1"
        browser.get(link)

        insert = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea")))        
        answer = math.log(int(time.time()))
        insert.send_keys(str(answer))

        button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button.click()

        output = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )

        assert output.text == "Correct!", f"Unexpected answer: {output}"
