#!/usr/bin/env python
import requests
import time
import os  
from bs4 import BeautifulSoup as soup
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options

from article import Article
# All articles go into this list, which holds Article Objects. 
articleList = []

def parsingSite(urls,siteName = ''):
	count = 0
	for url in urls:
		chrome_options = Options()  
		chrome_options.add_argument("--headless")  
		chrome_options.add_argument("--no-sandbox")
		chrome_options.add_argument("window-size=1120,550")
		browser = webdriver.Chrome(chrome_options=chrome_options)
		
		# browser = webdriver.Chrome()
		# # browser.set_window_size(1120, 550)
		browser.implicitly_wait(20)
		print(url)
		browser.get(url)
		innerHTML = browser.execute_script("return document.body.innerHTML") 

		# # returns the inner HTML as a string
		# time.sleep(.200)
		# with open('output{0}.txt'.format(count),'w') as myfile:
		# 	for line in innerHTML:
		# 		myfile.write(line)
		# time.sleep(.200)
		# with open('output{0}.txt'.format(count), 'r') as myfile:
		#     data=myfile.read().replace('\n', '')
		
		# page_soup = soup(data, 'html.parser')
		page_soup = soup(innerHTML, 'html.parser')
		count += 1

		# browser.close()
		baahrakhari(page_soup)

def baahrakhari(page_soup):
	
	site_section = page_soup.find(id="site-section")
	news_items = site_section.find_all(class_="page-news-list")
	news_1 = news_items[0]
	list_items = news_1.find_all('li')

	for lis in list_items:
		h3_item = lis.find('h3')
		# print(h3_item)
		if (h3_item and lis.find('img')) != None:
			link = (h3_item.find('a').get('href'))
			# link_.append(link)
			imageLink = lis.find('img')['data-original']
			# imageLink_.append(imageLink)
			description = (lis.find('p').get_text())
			# description_.append(description)
			title = (h3_item.find('a').get_text())
			# title_.append(title)
			makeArticleObject('Baahrakhari',title,description,link,imageLink)
		# Only if there are some inconsistency problems. 
		# else:
		# 	link_.append("None")
		# 	description_.append("None")
		# 	title_.append("None")
		# 	imageLink_.append("None")

# def kantipur(page_soup):

# def printTest(link_,imageLink_,description_,title_):
# 	print('Link: ' + str(len(link_)))
# 	print('ImageLink: ' + str(len(imageLink_)))
# 	print('Description: ' + str(len(description_)))
# 	print('Title:' + str(len(title_)))
# 	print('\n')
# 	print(link_[0:3])
# 	print(imageLink_[0:3])
# 	print(description_[0:3])
# 	print(title_[0:3])

def articleObjectTest():
	for items in articleList:
		print(items.info())

def makeArticleObject(source,title,description,link,imgLink):
	article = Article(title, description, link, imgLink, source)
	articleList.append(article)
	# print('-Article')

def main():

	b12_baseUrl = 'http://baahrakhari.com/'
	b12_categories = ['special-news/1/%E0%A4%B5%E0%A4%BF%E0%A4%B6%E0%A5%87%E0%A4%B7','news-article/1/Politics','news-article/2/Economy','news-article/3/Sports','news-article/4/Interview','news-article/6/Thought','news-article/7/Country','news-article/8/12khari-samikchya','news-article/9/Literature','news-article/12/Blog','news-article/14/Editorial','news-article/15/Foreign']
	b12_url = [b12_baseUrl + url for url in b12_categories]
	parsingSite(b12_url)

	# articleObjectTest()
	print(len(articleList))
	for article in articleList[0:3]:
		print('')
		print(article.info())

"""
TODO:
Kantipur = has e-paper option. Should add link to that in the app for user's option

Setopati = has continuous scrolling and pagination loading of articles, need to consider doing the first 15 - 20 articles for each parse.  (assuming that top most news is the newest. Otherwise will require a new way to figure this out)

Nagarik = structure of html doesnt seem to be general for all the news on theri catgory pages needs checking for confirmation
"""

# TODO: Anothoer list for passting search values for each news site. 
## Parsing tags for article. 

	siteList = ['kantipur','ktmpost','setopati','nagariknews','republica']


	baseUrlDict = {'kantipur':'https://www.kantipurdaily.com','ktmpost':'http://kathmandupost.ekantipur.com/category','':'setopati':'https://setopati.com','nagarik':'http://nagariknews.com/','republica':'http://www.myrepublica.com/'}

	siteCategoryDict = {'kantipur': ['/news','/business','/opinion','/sports','/national','/koseli','/world','/entertainment','/blog','/feature','/photo_feature','/lifestyle','/literature','/technology','/health','/Interview','/pathakmanch'], 'ktmpost': ['/general','/national','/capital','/silver-linings','/sports','/editorial','/oped','/photo-feature','/interview','/entertainment','/world','/blog','/escalate','/'], 'setopati': ['/politics','/social','/opinion','/entertainment','/sports','/setopati-blog','/literature','/global','/photo-gallery'],'nagariknews':['/category/21','/category/22','/category/24','/category/25','/category/26','/category/27','/category/28','/category/33','/category/81','/category/82'],'republica':['/category/23','/category/22','/category/24','/category/26','/category/27','/category/81','/category/35','/category/117','/category/137']}


if __name__== "__main__":
	main()