#!/usr/bin/python3

import re

subor = "20180701"

#Read the text file
with open(subor) as f:
	#Skip the first line (header)
	next(f)
	#Read first 100 lines of the file
	text = [next(f) for x in range(100)]
	for line in text:
		#Perform REGEX Search
		match = re.search(r'(?P<Rank>\d+)\s+(?P<Name>.*)\$(?P<Cap>[0-9,.]+)\s+\$(?P<Price>[0-9.,]+).*\$(?P<Volume>[0-9,]+)',line)
		#Print the found bits
		try:
			meno = re.search(r'.*\s+(?P<Tick>\w+)',match.group('Name'))
			print(match.group('Rank'), meno.group('Tick'), match.group('Cap'), match.group('Price'), match.group('Volume'))
		except:
			print("No match")
