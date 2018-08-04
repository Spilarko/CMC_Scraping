#!/usr/bin/python3

import re
import pymysql.cursors

subor = "20180701"


#Let's open a database
try:
	conn = pymysql.connect(host='127.0.0.1',user='root',password='Matisko',db='CMC')
	

	#Read the text file
	with open(subor) as f:

		#Skip the first line (header)
		next(f)

		#Read first 100 lines of the file
		text = [next(f) for x in range(100)]
		for line in text:
			#Perform REGEX Search
			match = re.search(r'(?P<Rank>\d+)\s+(?P<Name>.*)\$(?P<Cap>[0-9,.]+)\s+\$(?P<Price>[0-9.,]+).*\$(?P<Volume>[0-9,]+)',line)
			
			#Store the parsed information into Database
			try:
				meno = re.search(r'.*\s+(?P<Tick>\w+)',match.group('Name'))
				with conn.cursor() as cursor:
                			sql = "insert into Tickers (Id, Ticker, MktCap, Price, Volume, Day) VALUES (%s, %s, %s, %s, %s, %s)"
                			cursor.execute(sql,(match.group('Rank'),meno.group('Tick'),match.group('Cap'),match.group('Price'),match.group('Volume'),)
                			conn.commit()

				#print(match.group('Rank'), meno.group('Tick'), match.group('Cap'), match.group('Price'), match.group('Volume'))
			except:
				print("No match")

finally:
        conn.close()

