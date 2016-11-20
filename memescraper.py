import httplib
import re
import urllib2
import json
import time
import sys

# Initialize location and file name
fileName = "memes"
location = ""

if len(sys.argv) > 1:
	location = sys.argv[1] + '/'
if len(sys.argv) > 2:
		fileName = sys.argv[2]

if not fileName.endswith(".txt"):
	fileName += ".txt"
location += fileName 

# Pages to scrape
scrapePages = 1388
# Time in seconds 
sleepTime = 1 

def scrape(page):
    # Open up a connection and read the HTML contents of the page
	connection = httplib.HTTPConnection("www.quickmeme.com")
	connection.request("GET", "/memes/page/{0}/".format(page))
	response1 = connection.getresponse()
	data1 = response1.read()

    # Convert our matches list into a set as we don't want duplicate entries
	memes = set(re.findall('http\://s\.quickmeme\.com/img/.*\.jpg', data1))

    # Write the contents of the memes set into our file
	file = open(location, 'a')
	for meme in memes:
		file.write(meme + '\n')
	file.close()

# Clear our file
open(location, 'w+').close()

# SCRAPE!
for i in range(scrapePages):
	scrape(i)
	time.sleep(sleepTime)