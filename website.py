class Website(object):
	"""
	Website: object for parsing directions for given website.
	"""

	siteList = ['kantipur','ktmpost','setopati','nagariknews','republica']


"""
TODO:
Kantipur = has e-paper option. Should add link to that in the app for user's option

Setopati = has continuous scrolling and pagination loading of articles, need to consider doing the first 15 - 20 articles for each parse.  (assuming that top most news is the newest. Otherwise will require a new way to figure this out)

Nagarik = structure of html doesnt seem to be general for all the news on theri catgory pages needs checking for confirmation
"""

# TODO: Anothoer list for passting search values for each news site. 
## Parsing tags for article. 

	baseUrlDict = {'kantipur':'https://www.kantipurdaily.com','ktmpost':'http://kathmandupost.ekantipur.com/category','':'setopati':'https://setopati.com','nagarik':'http://nagariknews.com/','republica':'http://www.myrepublica.com/'}

	siteCategoryDict = {'kantipur': ['/news','/business','/opinion','/sports','/national','/koseli','/world','/entertainment','/blog','/feature','/photo_feature','/lifestyle','/literature','/technology','/health','/Interview','/pathakmanch'], 'ktmpost': ['/general','/national','/capital','/silver-linings','/sports','/editorial','/oped','/photo-feature','/interview','/entertainment','/world','/blog','/escalate','/'], 'setopati': ['/politics','/social','/opinion','/entertainment','/sports','/setopati-blog','/literature','/global','/photo-gallery'],'nagariknews':['/category/21','/category/22','/category/24','/category/25','/category/26','/category/27','/category/28','/category/33','/category/81','/category/82'],'republica':['/category/23','/category/22','/category/24','/category/26','/category/27','/category/81','/category/35','/category/117','/category/137']}

	def __init__(self, websiteName=""):
		self.websiteName = websiteName

	def getUrls(self, websiteName):
		"""
		To get all category urls for parsing
		"""
		baseUrlDict[websiteName]
