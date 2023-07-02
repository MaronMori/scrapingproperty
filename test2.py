from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13101&sc=13205&cb=0.0&ct=9999999&et=9999999&md=03&md=09&cn=10&mb=0&mt=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&srch_navi=1'
browser.get(url)

elements = browser.find_elements(By. CLASS_NAME, "cassetteitem_other-emphasis")
for element in elements:
    print(element.text)

