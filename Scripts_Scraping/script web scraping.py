#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from bs4 import BeautifulSoup
import requests as re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import requests
import pickle
import time
import json


# Login from Cookies
base_url = "https://shopee.co.id/mall/search?keyword"
keyword = "=apple%20iphone"
page_number = 0 # ganti nama halaman, 1 itu 0, 2 itu 1 dst
shop_id = 255563049 # ganti nama toko

url = f"{base_url}{keyword}&page={page_number}&pdpL3Category=0&shop={shop_id}"
driver = webdriver.Chrome()
driver.get(url)

# Load saved session cookies from file using pickle
with open('shopee_log.pkl', 'rb') as f:
    session_cookies = pickle.load(f)
    
# Add the loaded session cookies to the WebDriver instance
for cookie in session_cookies:
    driver.add_cookie(cookie)
# login
driver.get(url)
# find container
container = driver.find_element(By.CLASS_NAME, 'shopee-search-item-result__items')
# class
scroll = 'window.scrollTo(0, document.body.scrollHeight);'
scroll_page = 'window.scrollTo(0, 1080)'
title_class = 'ie3A+n bM+7UW Cve6sh'
ori_class = 'vioxXd ZZuLsr d5DWld'
discount_class = 'ZEgDH9'
sell_class = 'r6HknA uEPGHT'
sell_class_2 = 'r6HknA'
# create empty list
title_iphone, original_prices, discount_prices, sold_count, sold_count_2 = [], [], [], [], []

# scrape nama iphone
driver.execute_script(f"{scroll_page}") # scrolling the page
time.sleep(2) # give 2 seconds pause before scraping

titles = WebDriverWait(container, 60).until(
    EC.presence_of_all_elements_located((By.XPATH, f'//div[@class="{title_class}"]'))
) 
for title in titles:
    judul = title.text
    title_iphone.append(judul)
# check length (nama iphone, harus sama dengan yang discrape)
len(title_iphone)

ori_prices_2 = [0] * 18
# scrape harga iphone (yang dicoret atau harga aslinya)
driver.execute_script(f"{scroll_page}") # scrolling the page
time.sleep(2) # give 2 seconds pause before scraping

#prices original
ori_prices = driver.find_elements(By.XPATH, f'//div [@class="{ori_class}"]')
for ori in ori_prices:
    harga = ori.text
    original_prices.append(harga)
    
len(original_prices)
concat_ori_prices = original_prices + ori_prices_2
len(concat_ori_prices)

# scrape harga iphone saat ini (current  price)
driver.execute_script(f"{scroll_page}") # scrolling the page
time.sleep(2) # give 2 seconds pause before scraping
dis_prices = container.find_elements(By.XPATH, f'//span [@class="{discount_class}"]')

for dis in dis_prices:
    discount = dis.text
    discount_prices.append(discount)

len(discount_prices)

# scrape berapa banyak iphone yang terjual
driver.execute_script(f"{scroll_page}") # scrolling the page
time.sleep(2) # give 2 seconds pause before scraping

sold_product = container.find_elements(By.XPATH, f'//div [@class="{sell_class}"]')

for sold in sold_product:
    terjual = sold.text
    if terjual is None or terjual == "":
        terjual = "N/A"
    sold_count.append(terjual)

len(sold_count)

# scrape berapa banyak iphone yang terjual (class kedua)

driver.execute_script(f"{scroll_page}") # scrolling the page
time.sleep(2) # give 2 seconds pause before scraping

sold_product_2 = container.find_elements(By.XPATH, f'//div [@class="{sell_class_2}"]')

for sold in sold_product_2:
    terjual = sold.text
    if terjual is None or terjual == "":
        terjual = "N/A"
    sold_count_2.append(terjual)

len(sold_count_2)

combined_sold_count = sold_count + sold_count_2
# recheck len(harus sama semua)
len(combined_sold_count)
len(title_iphone)
len(concat_ori_prices)
len(discount_prices)
# list kolom
list_kolom = ['title_iphone', 'concat_ori_prices', 'discount_prices', 'combined_sold_count']
# buat data yang discrape tadi menjadi dictionary
dict_data = dict(zip(list_kolom,
                    (title_iphone,
                    concat_ori_prices,
                    discount_prices,
                    combined_sold_count)))
# re-check type data (harus dict)
type(dict_data)
# buat dataframe dari dictionary
df = pd.DataFrame(dict_data)
# ubah df ke csv
df.to_csv('iphone_ibox.csv')




