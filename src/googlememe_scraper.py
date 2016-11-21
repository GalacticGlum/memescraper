from bs4 import BeautifulSoup
import requests
import urllib
import time
import json

class GoogleMemeScraper():

	def __init__(self):
		self.header = { 'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36" }
		self.baseUrl = "https://www.google.com/search?q={0}&source=lnms&tbm=isch"
		self.query_set = self.__load_queryset()

	def __scrape_query(self, query):
		if query == "":
			print ("GoogleMemeScraper::scape_query: query value was empty!")
			return

		query_url = self.baseUrl.format(query)
		page = BeautifulSoup(urllib.request.urlopen(urllib.request.Request(query_url, headers = self.header)), 'html.parser')

		links = []
		for attribute in page.find_all("div", {"class" : "rg_meta"}):
		    links.append(json.loads(attribute.text)["ou"])

		return links

	def start(self, sleepTime, queriesAmount = -1):
		scrapedLinks = []
		
		if queriesAmount == 0:
			return scrapedLinks

		if queriesAmount < 0:
			queriesAmount = len(self.query_set)

		for i in range(queriesAmount):
			scrapedLinks += self.__scrape_query(self.query_set[i])
			time.sleep(sleepTime)

		return scrapedLinks

	def __load_queryset(self):
		with open('data/google_queryset.json') as file:
			contents = file.read()
			jsonobject = json.loads(contents)

			query_list = []
			for query in jsonobject:
				query_list.append(urllib.parse.quote(query))

			return query_list
