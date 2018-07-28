#!/usr/bin/python3

from urllib.request import urlopen
import time

subor = "CMC_URLs.txt"

#Read the text file with CMC snapshot links first
with open(subor) as f:
	for line in f:
		print (line, end='')
		html = urlopen(line)
		print(html.read())
		
		#Let's wait a second before fetching another site not look like DOS attack
		time.sleep(1)
		
