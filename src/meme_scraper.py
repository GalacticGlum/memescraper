import time
import sys
import argparse

import quickmeme_scraper
import googlememe_scraper 

location = ""

def main(argv):
    startTime = time.time()

    quick_scraper = quickmeme_scraper.QuickMemeScraper()
    quick_scraper.scrape_event.append(on_scrape)

    google_scraper = googlememe_scraper.GoogleMemeScraper()
    google_scraper.scrape_event.append(on_scrape)

    global location 
    fileName = "memes"

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', help='location')
    parser.add_argument('-fn', help='filename')
    parser.add_argument('-sl', help='shorten links', action='store_true')
    parser.add_argument('-debug', help='print debug information', action='store_true')
    parser.add_argument('-p', help='amount of pages to scrape from quickmeme. Defaults to: \'1388\'', default=1388)
    parser.add_argument('-q', help='amount of queries (from query set) to scrape from google. Defaults to: scrape all queries in query set', default=-1)
    parser.add_argument('-sleep', help='amount of time (seconds) to sleep after a scrape. Defaults to: \'1\'', default=1)

    args = parser.parse_args(argv[1:])
    shortenLinks = args.sl

    if args.l:
	    location = args.l + '/'
    if args.fn:
	    fileName = args.fn

    if args.p:
	    pageAmount = args.p

    if args.q:
	    queryAmount = args.q

    if not fileName.endswith(".txt"):
	    fileName += ".txt"

    print (location)
    location += fileName 
    open(location, 'w+').close()
	
    links = set(google_scraper.start(args.sleep, shortenLinks, int(queryAmount)) + quick_scraper.start(args.sleep, shortenLinks, int(pageAmount)))
    if args.debug:
	    scrapedMemes = len(links)
	    totalTime = (time.time() - startTime)

	    print ("Total Scraped Memes: {0}".format(len(links)))
	    print ("Elapsed Scrape Time: {:.2} minutes".format(totalTime / 60))
	    print ("Memes Per Second: {:d} memes/sec".format(int(scrapedMemes / totalTime)))

def dump_to_file(filename, contents):
	with open(filename, 'a') as file:
		for line in contents:		
			file.write(line + "\n")

def on_scrape(scraped_contents):
	dump_to_file(location, scraped_contents)

if __name__ == '__main__':
	main(sys.argv)