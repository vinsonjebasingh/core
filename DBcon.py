#Database connection
import MySQLdb
from config import *


class DBcon:
	
	def dbconnection(self): # database connection
		try:
			return MySQLdb.connect(hostname,username,password,database)
		except Exception as e:
			print ("Could not connect:", e)		

	def viewdata(self, qry ): # View records from table
		db=DBcon.dbconnection(self)
		cursor = db.cursor()
		try:
			cursor.execute(qry)
		except Exception as e:
			print (e)
		try:
			data = cursor.fetchall()
			for row in data:
				empid = row[0]
				name = row[1]
				email = row[2]
				contact = row[3]
				address = row[4]
				pincode = row[5]
				print ("Employee ID=%d,Name=%s,Email=%s,Contact No=%s,Address=%s,Pincode=%d" % \
				(empid, name, email, contact, address, pincode))
		except Exception as e:
			print ("Error:",e)
		db.close()

	def insertdata(self, qry ): # Insert records into table
		db=DBcon.dbconnection(self)
		cursor = db.cursor()
		try:
			cursor.execute(qry)
			db.commit()
			print (cursor.lastrowid)
		except Exception as e:
			db.rollback()
			print (e)
		db.close()

	def deleterecord(self, qry): # Delete Records from table
		db=DBcon.dbconnection(self)
		cursor = db.cursor()
		try:
			cursor.execute(qry)
			db.commit()
		except Exception as e:
			db.rollback()
			print (e)
		db.close()

	def update_record(self, qry): # Update records
		db=DBcon.dbconnection(self)
		cursor = db.cursor()
		try:
			cursor.execute(qry)
			db.commit()
			print (cursor.lastrowid)
		except Exception as e:
			db.rollback()
			print (e)
		db.close()
