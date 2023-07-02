from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
url = "https://suumo.jp/chintai/tokyo/city/"
browser.get(url)

tokyo_locations = browser.find_elements(By.CSS_SELECTOR, '.searchitem-list > li > label > span:first-of-type')
tokyo = []
for tokyo_location in tokyo_locations:
    tokyo.append(tokyo_location.text)
print(tokyo)


x = browser.find_elements(By.CSS_SELECTOR, '.searchitem-list > li')
for y in x:
    print(y.text)
