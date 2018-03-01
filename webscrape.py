#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from article import Article

# All articles go into this list, which holds Article Objects. 
articleList = []

def parsing_Site(url):
	# browser.get(url)
	# innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string

	# with open('output1.txt','wb') as myfile:
	# 	myfile.write(str(innerHTML))

	with open('innerHTML.txt', 'r') as myfile:
	    data=myfile.read().replace('\n', '')
	page_soup = soup(data, 'html.parser')

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

def main():
	# title_ = []
	# link_  = []
	# imageLink_ = []
	# description_ = []

	#browser = buildDriver()
	# browser = webdriver.Chrome()
	# browser.implicitly_wait(10)

	b_baseUrl = 'http://baahrakhari.com/'
	b12_categories = ['special-news/1/%E0%A4%B5%E0%A4%BF%E0%A4%B6%E0%A5%87%E0%A4%B7','news-article/1/Politics','news-article/2/Economy','news-article/3/Sports','news-article/4/Interview','news-article/6/Thought','news-article/7/Country','news-article/8/12khari-samikchya','news-article/9/Literature','news-article/12/Blog','news-article/14/Editorial','news-article/15/Foreign']
	b12_sites = [urls + b_baseUrl for urls in b12_categories]
	parsing_Site(b12_sites)

	articleObjectTest()


if __name__== "__main__":
	main()