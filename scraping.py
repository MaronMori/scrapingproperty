from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd
import os


def generate_unique_filename(filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    while os.path.exists(filename):
        filename = f"{base}_{counter}{ext}"
        counter += 1
    return filename


def scraping(location_box, age_box, distance_box, size_box, min_rent_box, max_rent_box, number_of_house_box):
    location = location_box.get()
    age = age_box.get()
    distance = distance_box.get()
    size = size_box.get()
    min_rent = min_rent_box.get()
    max_rent = max_rent_box.get()

    number_of_houses = {"5件以下": 5, "10件以下": 10, "20件以内": 20, "30件以内": 30, "40件以内": 40, "50件以内": 50, "100件以内": 100}
    selected_number = number_of_house_box.get()  # 指定された数字を取得
    selected_value = number_of_houses[selected_number]  # 指定された数字の要素を取得

    browser = webdriver.Chrome()
    url = "https://suumo.jp/chintai/tokyo/city/"
    browser.get(url)
    actions = ActionChains(browser)
    sleep(2)

    wait = WebDriverWait(browser, 10)

    # 地区
    tokyo_locations = browser.find_elements(By.CSS_SELECTOR, '.searchitem-list > li')
    if location:
        for tokyo_location in tokyo_locations:
            if location in tokyo_location.text:
                tokyo_location_input = tokyo_location.find_element(By.TAG_NAME, "input")
                tokyo_location_input_id = tokyo_location_input.get_attribute("id")
                checkbox = browser.find_element(By.ID, tokyo_location_input_id)

                checkbox.click()

    scroll = browser.find_element(By.XPATH, "//*[@id='js-shiborikomiForm']/div/div[2]/div[2]/table/tbody/tr[6]")
    actions.move_to_element(scroll).perform()
    sleep(2)

    # 築年数
    if age != "指定しない":
        tokyo_age = browser.find_element(By.XPATH, f"//li[label[contains(text(), '{age}')]]")
        tokyo_age_input = tokyo_age.find_element(By.TAG_NAME, 'input')
        tokyo_age_input.click()

    # 間取り
    if size:
        tokyo_size = browser.find_element(By.XPATH, f"//li[label[contains(text(), '{size}')]]")
        tokyo_size_input = tokyo_size.find_element(By.TAG_NAME, 'input')
        tokyo_size_input.click()

    # 駅徒歩
    if distance != "指定しない":
        tokyo_distance = browser.find_element(By.XPATH, f"//li[label[contains(text(), '{distance}')]]")
        tokyo_distance_input = tokyo_distance.find_element(By.TAG_NAME, 'input')
        tokyo_distance_input.click()

    # 家賃
    if min_rent != "下限なし":
        min_rent_select = browser.find_element(By.XPATH, "//select[@name='cb']")
        min_rent_select.click()
        min_option = browser.find_element(By.XPATH, f"//option[contains(text(), '{min_rent}')]")
        min_option.click()
    if max_rent != "上限なし":
        max_rent_select = browser.find_element(By.XPATH, "//select[@name='ct']")
        max_rent_select.click()
        max_option = browser.find_element(By.XPATH, f"//option[contains(text(), '{max_rent}')]")
        max_option.click()

    search = browser.find_element(By.XPATH, "//a[text()= 'この条件で検索する']")
    search.click()
    sleep(3)

    each_room = browser.find_element(By.XPATH, "//*[@id='js-leftColumnForm']/div[2]/ul/li[2]/div")
    each_room.click()

    # 検索結果があるかどうか確かめる
    try:
        element = browser.find_element(By.CLASS_NAME, "property_group")
    except NoSuchElementException:
        print("物件が見つかりませんでした。")
        return

    # cvsに書き出すためのデータフレーム
    df = pd.DataFrame()

    rent_prices = []
    management_fees = []
    deposit_fees =[]
    key_monies = []
    size_houses = []
    ages_house = []
    distances = []
    addresses = []
    name_houses = []
    url_houses = []
    pictures_house = []

    prices_list = []
    manage_fee_list = []
    deposit_fee_list = []
    key_money_list = []
    size_house_list = []
    age_house_list = []
    distance_list = []
    address_list = []
    name_house_list = []
    url_house_list = []
    picture_list = []

    # 指定した物件数まで取得する。超えた場合はループを抜けて超過分を削除
    while len(rent_prices) < selected_value:
        rent_prices = browser.find_elements(By.CLASS_NAME, 'detailbox-property-point')
        management_fees = browser.find_elements(By.CSS_SELECTOR, 'tr > td.detailbox-property--col1 > div:nth-child(2)')
        deposit_fees = browser.find_elements(By.CSS_SELECTOR, '.detailbox-property--col2 > div:nth-child(1)')
        key_monies = browser.find_elements(By.CSS_SELECTOR, '.detailbox-property--col2 > div:nth-child(2)')
        size_houses = browser.find_elements(By.XPATH, f"//tr/td/div[contains(text(), '{size}')]")
        ages_house = browser.find_elements(By.XPATH, '//td/div[contains(text(), "築")]')
        distances = browser.find_elements(By.CSS_SELECTOR, '.detailnote > .detailnote-box:nth-child(1)')
        addresses = browser.find_elements(By.CSS_SELECTOR, 'div.detailbox-property > table > tbody > tr > td:nth-child(5)')
        name_houses = browser.find_elements(By.CLASS_NAME, 'property_inner-title')
        url_houses = browser.find_elements(By.CSS_SELECTOR, '.property_inner-title > a')
        pictures_house = browser.find_elements(By.CSS_SELECTOR, ".cassette_carrousel > .cassette_carrousel-thumblist > .cassette_carrousel-item > li > img")

        rent_prices = rent_prices[:selected_value]
        management_fees = management_fees[:selected_value]
        deposit_fees = deposit_fees[:selected_value]
        key_monies = key_monies[:selected_value]
        size_houses = size_houses[:selected_value]
        ages_house = ages_house[:selected_value]
        distances = distances[:selected_value]
        addresses = addresses[:selected_value]
        name_houses = name_houses[:selected_value]
        url_houses = url_houses[:selected_value]
        pictures_house = pictures_house[:selected_value]

        # 家賃
        for rent_price in rent_prices:
            prices_list.append(rent_price.text)
            print(rent_price.text)
        df['家賃'] = prices_list
        # 管理費
        for management_fee in management_fees:
            manage_fee_list.append(management_fee.text)
            print(management_fee.text)
        df['管理費'] = manage_fee_list
        # 敷金
        for deposit_fee in deposit_fees:
            deposit_fee_list.append(deposit_fee.text)
            print(deposit_fee.text)
        df['敷金'] = deposit_fee_list
        # 礼金
        for key_money in key_monies:
            key_money_list.append(key_money.text)
            print(key_money.text)
        df['礼金'] = key_money_list
        # 間取り
        for size_house in size_houses:
            size_house_list.append(size_house.text)
            print(size_house.text)
        df['間取り'] = size_house_list
        # 築年数
        for age_house in ages_house:
            age_house_list.append(age_house.text)
            print(age_house.text)
        df['築年数'] = age_house_list
        # 駅徒歩
        for distance_from_subway in distances:
            distance_list.append(distance_from_subway.text)
            print(distance_from_subway.text)
        df['駅徒歩'] = distance_list
        # 住所
        for address in addresses:
            address_list.append(address.text)
            print(address.text)
        df['住所'] = address_list
        # 物件の名前
        for name_house in name_houses:
            name_house_list.append(name_house.text)
            print(name_house.text)
        df['物件名'] = name_house_list
        # 物件のURL
        for url_house in url_houses:
            url_of_the_house = url_house.get_attribute("href")
            url_house_list.append(url_of_the_house)
            print(url_of_the_house)
        df["物件のURL"] = url_house_list
        # 写真
        for picture_house in pictures_house:
            picture_list.append(picture_house.get_attribute('src'))
            print(picture_house.get_attribute('src'))
        df['写真'] = picture_list

        if len(rent_prices) > selected_value:
            break
        try:
            wait_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div/div/p/a[contains(text(), '次へ')]")))
            try:
                next_page = browser.find_element(By.XPATH, "//div/div/p/a[contains(text(), '次へ')]")
                next_page.click()
            except NoSuchElementException:
                break
        except TimeoutException:
            break
        sleep(2)

    output_filename = f'物件情報_{location}_{age}_{distance}_{size}_{min_rent}-{max_rent}.csv'
    output_filename = generate_unique_filename(output_filename)
    df.to_csv(output_filename, encoding='utf-8', index=False)
