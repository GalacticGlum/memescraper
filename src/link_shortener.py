import http
import json

# Load API key
api_key = ""
with open('data/api_key.auth') as file:
	api_key = file.readline()

def shorten_url(url):
	if api_key:
		connection = http.client.HTTPSConnection("www.googleapis.com")
		body = json.dumps({'longUrl': url})
		headers = {'Content-Type': 'application/json'}
		connection.request("POST", "/urlshortener/v1/url?key={0}".format(api_key), body, headers)
		response = connection.getresponse()
		jsonresponse = response.read().decode('utf-8')

		try:
			if 'id' in json.loads(jsonresponse):
				return json.loads(jsonresponse)['id']
			else:
				print("link_shortner::shorten_url: Could not shorten url: {0} .".format(url))
				return url
		except:
			print("link_shortner::shorten_url: Could not shorten url: {0} .".format(url))
	else:
		print("link_shortner::shorten_url: Authentication failure: no Google API key provided. Make sure 'data/api_key.auth' exists and contains the api key on line '1'!")
		return url


def shorten_urls(urls):
	if api_key:
		results = []
		for url in urls:
			results.append(shorten_url(url))
		return results
	else:
		print("link_shortner::shorten_urls: Authentication failure: no Google API key provided. Make sure 'data/api_key.auth' exists and contains the api key on line '1'!")
		return urls


