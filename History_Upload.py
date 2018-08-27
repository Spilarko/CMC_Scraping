#!/usr/bin/python3

#Pouzite na upload CMC historie v CSV do databazy

import csv
import pymysql.cursors
from datetime import datetime

try:
	conn = pymysql.connect(host='127.0.0.1',user='hello',password='Hello123!',db='CMC')
	
	with open('test.csv') as csv_file, conn.cursor() as cursor:
#		next(csv_file)
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			#2-Ticker , 3-Date, 7-Close, 8-Volume, 9-MarketCap
			ticker = row[2]
			datum = datetime.strptime(row[3],'%Y-%m-%d %H:%M:%S.%f').date()
			close = float(row[7])
			volume = int(float(row[8]))
			marketCap = int(row[9])
			print(ticker,datum,close,volume,marketCap)
			sql = "insert into Tickers (Id, Ticker, MktCap, Price, Volume, Day) VALUES (%s, %s, %s, %s, %s, %s)"
			cursor.execute(sql,(row[0],ticker,marketCap,close,volume,datum))
			conn.commit()

finally:
	conn.close()
