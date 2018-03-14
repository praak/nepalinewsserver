import requests
import time
import os  
from bs4 import BeautifulSoup as soup
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options

from article import Article


# url = 'https://www.kantipurdaily.com/news'

# browser = webdriver.Chrome()
# # browser.set_window_size(1120, 550)
# browser.implicitly_wait(10)
# # print(url)
# browser.get(url)
# innerHTML = browser.execute_script("return document.body.innerHTML")

count = 0
# with open('kantipur{0}.txt'.format(count),'w') as myfile:
# 	for line in innerHTML:
# 		myfile.write(line)

with open('kantipur{0}.txt'.format(count), 'r') as myfile:
		    data=myfile.read().replace('\n', '')
		
page_soup = soup(data, 'html.parser')

# print(page_soup.prettify())

site_section = page_soup.find(class_="listLayout")
news_items = site_section.find_all('article',class_='normal')
# lis_items = news_items.find_all('div')

for news in news_items[0:3]:
	print(news)

# for lis in lis_items[0:5]:
# 	print(lis)
