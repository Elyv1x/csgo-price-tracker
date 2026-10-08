from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from item import Item
import pandas as pd
import time

def scrape_one_url(driver, url):
    driver.get(url)

    wait = WebDriverWait(driver, 20)

    rows = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tr.ant-table-row.ant-table-row-level-0"))
    )

    prices = []
    name_div = rows[0].find_element(By.CSS_SELECTOR, "div[class*='commodity-title']")
    item_name = name_div.text.strip()

    for i in range(10):
        row = rows[i]
        
        price_span = row.find_element(By.CSS_SELECTOR, "td:nth-child(5) span")
        while price_span.text.strip() == "":
            time.sleep(0.25)
        
        prices.append(price_span.text)

    item1 = Item(item_name, prices)
    return item1