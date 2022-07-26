#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# In[10]:


#* Full coding to scrape Hermes website to match keywords listed so product page with the bags we want will automatically load
#* timed interval set to auto-run the script every set timeframe (like 5 minutes) like 
### Auto-Schedule Python Scripts using Crontab
#* set ways to avoid IPs being blocked by Hermes

import requests
import datetime
import webbrowser

#Store script into a function
def func():
    
#* SET Parameters 
#chrome browser
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
#page you want to scrape
    url_to_scrape = 'https://www.hermes.com/ca/en/category/women/bags-and-small-leather-goods/bags-and-clutches/#|'
#keyword you want to match from parameters (contains)
    keyword_list = ['birkin', 'kelly', 'constance', 'picotin', 'lindy','evelyne']
#category in html source code you want to filter through
    parameter='product-item-meta-link'
#clear temp time log
    timestamp_list = []

    URL = url_to_scrape
    page = requests.get(URL)

#* This code issues an HTTP GET request to the given URL
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page.content, "html.parser")

#fill all products listed in the webpage in product list (manually discovered that all product listing has ID)
    product_list = []
    for URL in soup.find_all('a'):
        if URL.get('id') is not None:
#*        print(URL.get('href'))
            product_list.append(URL.get('href'))

    a = 'Total no. of product listed as of ' + str(datetime.datetime.now()) + " is "
    b =len(product_list)

    print(a + str(b))  
    timestamp_list.append(a + str(b))

#* loop through keyword list and product_list
    c = ' items match your keywords '
    urla = 'https://www.hermes.com'
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    final_url = []

    for i in keyword_list:
        for product in product_list:
            if i in product: 
                final_url.append(urla+product)
                print(str(len(final_url))+c)
                timestamp_list.append(str(len(final_url))+c+'as of '+ str(datetime.datetime.now()))
#load findings that match key terms in Chrome Browser
    for link in final_url:
        webbrowser.get(chrome_path).open(link)
                
#            webbrowser.get(chrome_path).open(urla+product)
#https://www.hermes.com/ca/en/product/hermes-cinhetic-clutch-H073654CKL3/            

#write timelog to timestamp_log.txt file
    with open(r'/Users/sandy/Timestamp_log.txt', 'a') as fp:
        for item in timestamp_list:
        # write each item on a new line
            fp.write(item+'\n')
        print('Done')


#https://www.geeksforgeeks.org/python-script-that-is-executed-every-5-minutes/

import schedule
import time

schedule.every(5).minutes.do(func)

while True:
	schedule.run_pending()
	time.sleep(1)