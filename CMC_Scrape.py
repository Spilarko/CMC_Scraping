#!/usr/bin/python3

import re

subor = "20180701.txt"

#Read the text file
with open(subor) as f:
	#Skip the first line (header)
	next(f)
	for line in f:
		#Perform REGEX Search
		match = re.search(r'(?P<Rank>\d+)\s+(?P<Name>.*)\$(?P<Cap>[0-9,.]+)\s+\$(?P<Price>[0-9.,]+).*\$(?P<Volume>[0-9,]+)',line)
		#Print the found bits
		try:
			print(match.group('Rank'), match.group('Name'), match.group('Cap'), match.group('Price'), match.group('Volume'))
		except:
			print("No match")
