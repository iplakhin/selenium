from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random

# Тест проверяет работу нескольких функций интернет магазина Wildberries:
#   Поиск товара через каталог;
#   Добавление товара в корзину;


link = "https://www.wildberries.ru/"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    menu = browser.find_element(By.CSS_SELECTOR, ".nav-element__burger")
    menu.click()
    time.sleep(3)

    categories = browser.find_elements(By.CSS_SELECTOR, ".menu-burger__main-list-link")
    category = random.choice(categories)
    browser.get(category.get_attribute("href"))
    time.sleep(3)

    sub_categories = browser.find_elements(By.CSS_SELECTOR, "a.j-menu-item")
    sub_category = random.choice(sub_categories)
    browser.get(sub_category.get_attribute("href"))
    time.sleep(5)

    goods = browser.find_elements(By.CSS_SELECTOR, "a.product-card__link")
    good = random.choice(goods)
    browser.get(good.get_attribute("href"))

    time.sleep(3)

    buy = browser.find_element(By.CSS_SELECTOR, "button.btn-main")
    buy.click()
    time.sleep(1)

    browser.get("https://www.wildberries.ru/lk/basket")
    time.sleep(3)

    count = browser.find_element(By.CSS_SELECTOR, "h1.basket-section__header").get_attribute("data-count")
    if int(count) > 0:
        print("Test PASSED!")
    else:
        print("Test FAILED!")


finally:
    time.sleep(5)
    browser.quit()