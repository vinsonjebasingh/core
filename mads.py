#maths class file
from types import *
class mads:

	def addition(self, parm1, parm2):
		try:
			if type(parm1) is int and type(parm2) is int:
				res = parm1 + parm2
				print (res)
		except Exception as e:
			raise e
	def substraction(self,parm1, parm2):
		try:
			if type(parm1) is int and type(parm2) is int:
				res = parm1-parm2
				print (res)
		except Exception as e:
			raise e
	def division(self,parm1, parm2):
		try:
			if type(parm1) is int and type(parm2) is int:
				res = parm1/parm2
				print (res)
		except Exception as e:
			raise e
	def multiplication(self,parm1, parm2):
		try:
			if type(parm1) is int and type(parm2) is int:
				res = parm1*parm2
				print (res)
		except Exception as e:
			raise e

m = mads()
