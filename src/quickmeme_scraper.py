import http
import re
import time

class QuickMemeScraper():

	def __init__(self):
		self.regexp = re.compile(r'http://s\.quickmeme\.com/img/[0-9a-f]{2}/[0-9a-f]*\.jpg')
		self.page = 0
		self.scrape_event = []

	def __scrape_page(self):
		# Open up a connection and read the HTML contents of the page
		connection = http.client.HTTPConnection("www.quickmeme.com")
		connection.request("GET", "/memes/page/{0}/".format(self.page))
		response = connection.getresponse()
		data = str(response.read())

		self.page += 1
		scraped_contents = set(re.findall(self.regexp, data))

		if self.shorten_links:
			links = link_shortener.shorten_urls(links)

		for callback in self.scrape_event:
			callback(scraped_contents)

		return scraped_contents

	def start(self, sleepTime, shorten_links, pageAmount = 1388):
		scrapedLinks = []
		self.shorten_links = shorten_links

		for i in range(pageAmount):
			scrapedLinks += self.__scrape_page()
			time.sleep(sleepTime)

		return scrapedLinks


