import http
import re
import time

class QuickMemeScraper():

	def __init__(self):
		self.regexp = re.compile(r'http://s\.quickmeme\.com/img/[0-9a-f]{2}/[0-9a-f]*\.jpg')
		self.page = 0

	def __scrape_page(self):
		# Open up a connection and read the HTML contents of the page
		connection = http.client.HTTPConnection("www.quickmeme.com")
		connection.request("GET", "/memes/page/{0}/".format(self.page))
		response = connection.getresponse()
		data = str(response.read())

		self.page += 1

		return set(re.findall(self.regexp, data))

	def start(self, sleepTime, pageAmount = 1388):
		scrapedLinks = []

		for i in range(pageAmount):
			scrapedLinks += self.__scrape_page()
			time.sleep(sleepTime)

		return scrapedLinks


