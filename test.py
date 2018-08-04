#!/usr/bin/python3

import pymysql.cursors

def getConnection():

	connection = pymysql.connect(host='127.0.0.1',user='root',password='Matisko',db='CMC')
	return connection

try:
	conn = getConnection()
	with conn.cursor() as cursor:
		#sql = "SELECT * FROM t20180701"
		sql = "insert into t20180701 (id, ticker, MktCap, Price, Volume) VALUES (%s, %s, %s, %s, %s)"
		cursor.execute(sql,(2,'ETH',123456789,400.4,87654))
		conn.commit()		
		#for row in cursor:
		#	print (row)

finally:
	conn.close()
