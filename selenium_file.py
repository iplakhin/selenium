from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.CSS_SELECTOR, "[type='text'")
    for element in elements:
        element.send_keys("askjdfh")

    file = browser.find_element(By.CSS_SELECTOR, "#file")
    file_path = os.path.abspath(os.path.dirname(__file__)) + '\sample_file.txt'
    file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()