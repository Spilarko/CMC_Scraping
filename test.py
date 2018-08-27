#!/usr/bin/python3

import pymysql.cursors

def getConnection():

	connection = pymysql.connect(host='127.0.0.1',user='hello',password='Hello123!',db='CMC')
	return connection

try:
	conn = getConnection()
	with conn.cursor() as cursor:
		Mcap = '123,456,789'
		Mcap2 = Mcap.replace(",","")
		sql = "insert into Tickers (id, ticker, MktCap, Price, Volume) VALUES (%s, %s, %s, %s, %s)"
		cursor.execute(sql,(2,'ETH',int(Mcap2),400.4,87654))
		conn.commit()		
		#for row in cursor:
		#	print (row)

finally:
	conn.close()
