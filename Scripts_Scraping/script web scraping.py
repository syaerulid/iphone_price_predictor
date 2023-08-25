#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# # Login from Cookies

# In[2]:


base_url = "https://shopee.co.id/mall/search?keyword"
keyword = "=apple%20iphone"
page_number = 0 # ganti nama halaman, 1 itu 0, 2 itu 1 dst
shop_id = 255563049 # ganti nama toko


# In[3]:


url = f"{base_url}{keyword}&page={page_number}&pdpL3Category=0&shop={shop_id}"


# In[4]:


driver = webdriver.Chrome()
driver.get(url)


# In[5]:


# Load saved session cookies from file using pickle
with open('shopee_log.pkl', 'rb') as f:
    session_cookies = pickle.load(f)


# In[6]:


# Add the loaded session cookies to the WebDriver instance
for cookie in session_cookies:
    driver.add_cookie(cookie)


# In[7]:


driver.get(url)


# In[8]:


container = driver.find_element(By.CLASS_NAME, 'shopee-search-item-result__items')


# In[9]:


container


# In[10]:


scroll = 'window.scrollTo(0, document.body.scrollHeight);'
scroll_page = 'window.scrollTo(0, 1080)'
title_class = 'ie3A+n bM+7UW Cve6sh'
ori_class = 'vioxXd ZZuLsr d5DWld'
discount_class = 'ZEgDH9'
sell_class = 'r6HknA uEPGHT'
sell_class_2 = 'r6HknA'


# In[11]:


title_iphone, original_prices, discount_prices, sold_count, sold_count_2 = [], [], [], [], []


# In[12]:


# scrape nama iphone
driver.execute_script(f"{scroll_page}") # scrolling the page
time.sleep(2) # give 2 seconds pause before scraping

titles = WebDriverWait(container, 60).until(
    EC.presence_of_all_elements_located((By.XPATH, f'//div[@class="{title_class}"]'))
)
    
for title in titles:
    judul = title.text
    title_iphone.append(judul)


# In[13]:


len(title_iphone)


# In[17]:


ori_prices_2 = [0] * 18


# In[15]:


# scrape harga iphone (yang dicoret atau harga aslinya)
driver.execute_script(f"{scroll_page}") # scrolling the page
time.sleep(2) # give 2 seconds pause before scraping

#prices original
ori_prices = driver.find_elements(By.XPATH, f'//div [@class="{ori_class}"]')
for ori in ori_prices:
    harga = ori.text
    original_prices.append(harga)


# In[16]:


len(original_prices)


# In[18]:


concat_ori_prices = original_prices + ori_prices_2


# In[19]:


len(concat_ori_prices)


# In[20]:


# scrape harga iphone saat ini (current  price)
driver.execute_script(f"{scroll_page}") # scrolling the page
time.sleep(2) # give 2 seconds pause before scraping
dis_prices = container.find_elements(By.XPATH, f'//span [@class="{discount_class}"]')

for dis in dis_prices:
    discount = dis.text
    discount_prices.append(discount)


# In[21]:


len(discount_prices)


# In[22]:


# scrape berapa banyak iphone yang terjual

driver.execute_script(f"{scroll_page}") # scrolling the page
time.sleep(2) # give 2 seconds pause before scraping

sold_product = container.find_elements(By.XPATH, f'//div [@class="{sell_class}"]')

for sold in sold_product:
    terjual = sold.text
    if terjual is None or terjual == "":
        terjual = "N/A"
    sold_count.append(terjual)


# In[23]:


len(sold_count)


# In[24]:


# scrape berapa banyak iphone yang terjual (class kedua)

driver.execute_script(f"{scroll_page}") # scrolling the page
time.sleep(2) # give 2 seconds pause before scraping

sold_product_2 = container.find_elements(By.XPATH, f'//div [@class="{sell_class_2}"]')

for sold in sold_product_2:
    terjual = sold.text
    if terjual is None or terjual == "":
        terjual = "N/A"
    sold_count_2.append(terjual)


# In[25]:


len(sold_count_2)


# In[26]:


combined_sold_count = sold_count + sold_count_2


# In[27]:


len(combined_sold_count)


# In[28]:


len(title_iphone)


# In[29]:


len(concat_ori_prices)


# In[30]:


len(discount_prices)


# In[31]:


list_kolom = ['title_iphone', 'concat_ori_prices', 'discount_prices', 'combined_sold_count']


# In[32]:


dict_data = dict(zip(list_kolom,
                    (title_iphone,
                    concat_ori_prices,
                    discount_prices,
                    combined_sold_count)))


# In[33]:


type(dict_data)


# In[34]:


df = pd.DataFrame(dict_data)


# In[35]:


df


# In[36]:


df.to_csv('halaman_2_ibox.csv')


# In[ ]:




