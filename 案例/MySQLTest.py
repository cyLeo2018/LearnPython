#! /usr/bin/python3

import pymysql

db = pymysql.connect("localhost","testuser","test123","TESTDB")
cursor = db.cursor()
cursor.execute("select version()")
date = cursor.fetchone()

print("DBMS Version:%s" % data)

db.close()

