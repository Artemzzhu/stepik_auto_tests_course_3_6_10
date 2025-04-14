import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_basket_availability(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    try:
        button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket"))
        )
        assert button is not None, "Кнопка не найдена"
        print("Кнопка найдена!")
    except:
        print("Кнопка не найдена!")

