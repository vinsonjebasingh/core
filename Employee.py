#Employee registration

import MySQLdb
import DBcon
from DBcon import *

class Employee():
	def view_emp(self):
		qry = "SELECT * FROM employee"
		try:			
			dbobj = DBcon()
			dbobj.viewdata( qry )
		except Exception as e:
			print (e)
		
	def insert_emp(self):
		qry = "INSERT INTO employee(name,email_id,contact_no,address,pincode)values('%s','%s','%s','%s','%d')" %('Mani', 'mani@gmail.com', '9658748545','#454, Mount Road', 600001)
		try:			
			dbobj = DBcon()
			print (dbobj)
			dbobj.insertdata( qry )
		except Exception as e:
			print (e)

	def delete_emp(self, id):
		qry = "DELETE FROM employee WHERE id='%d'"% (id)
		try:			
			dbobj = DBcon()
			print (dbobj)
			dbobj.deleterecord( qry )
		except Exception as e:
			print (e)

	def update_emp(self, id):
		qry = "UPDATE employee SET name='%s', email_id='%s', contact_no='%s', address='%s', pincode='%d' WHERE id='%d'"% ('Ram kumar', 'ramkumar@gmail.com', '9855456587', '432, Anna Salai', 600032, id)
		try:			
			dbobj = DBcon()
			print (dbobj)
			dbobj.update_record( qry )
		except Exception as e:
			print (e)

emp = Employee()
#emp.insert_emp()
#emp.delete_emp(id = 10)
emp.update_emp(id = 12)
#emp.view_emp()

