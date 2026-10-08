import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from single_scraper import scrape_one_url
from item import Item
import time

def scrape_all():
    driver_path = "C:\\Users\\fh2po\\Downloads\\edgedriver_win64\\msedgedriver.exe"
    service = Service(driver_path)

    options = webdriver.EdgeOptions()
    options.add_argument(
        r"user-data-dir=C:\\Users\\fh2po\\EdgeSeleniumProfile" 
    )#被拦截了加的
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(service = service, options = options)

    os.system("cls")
    with open("C:\\Users\\fh2po\\Desktop\\Pro-ject1\\urls.txt", "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    results = []
    for url in urls:
        temp = scrape_one_url(driver, url)
        results.append(temp)

    driver.quit()

    #print(*results, sep = "\n")
    with open("C:\\Users\\fh2po\\Desktop\\Pro-ject1\\result.txt", "a", encoding="utf-8") as f:
        f.write(f"#时间: {datetime.now()}\n")
        for result in results:
            f.write(str(result) + "\n")
        f.write("\n")

os.system("cls")
for i in range(5):
    scrape_all()
    print(i+1, "-th time success")
    time.sleep(3*3600)