from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
url = "https://suumo.jp/chintai/tokyo/city/"
browser.get(url)

test = browser.find_element(By.XPATH, "//*[contains(text(), '10年以内')]")
print(test)
