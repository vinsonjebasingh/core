#mathematic calculation

from mads import*

class calculateVal:

	def calculate(self, method, parm1, parm2):
		cal_method = {'addition':'addition','substraction':'substraction','division':'division','multiplication':'multiplication'}
		if method in cal_method:
			method_name = str(cal_method[method])
			try:
				method_def = getattr(mads, method_name)
			except AttributeError:
				print (method_name, "not found")
			else:
				method_def(self,parm1,parm2)
		else:
			print ("This method does not exits")

c = calculateVal()
parm1 = 8
parm2 = 4
method = 'division' #addition, substraction, division, multiplication
c.calculate(method,parm1,parm2)


