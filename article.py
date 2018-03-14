class Article(object):

	def __init__(self, title = "", description ="", link = "", imageLink = "", source = "", category = ""):
		self.title = title
		self.description = description
		self.link = link
		self.imageLink = imageLink
		self.source = source
		self.category = category
		
	def info(self):
		information = ('Title: ' + self.title + '\n')
		# print('Description: ' + self.description '\n')
		information += ('Source: ' + self.source + '\n')
		information += ('Image Link: ' + self.imageLink)
		# print(information)

		return information

