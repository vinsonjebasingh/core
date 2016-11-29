# Write a program which will read a file from given path, calculate the size of the file and write it to another file.
# Also append timestamp, if the size of the file is greater than 1 MB then throw an error. Implement using try catch.
import os
import time
import datetime
class readFile:
	def fileProperties(self, f_name):
		f_path = os.path.abspath(f_name)
		statinfo = os.path.getsize(f_path)
		#1 mb equals to 1048576 ie (1024*1024) bytes
		mb = 1048576
		sizeOf_file = statinfo/(1024*1024)
		#1 MB is equal to 1,048,576 bytes or 1,024 Kilobytes
		ct = time.time()
		ts = datetime.datetime.fromtimestamp(ct).strftime('%Y-%m-%d %H:%M:%S')
		wsize = "Size : %s" %sizeOf_file
		wtimestamp = "\nTimestamp : %s" %ts
		if statinfo<mb:
			try:
				fo = open("properties.txt", "wb")
				fo.write(bytes(wsize,'UTF-8'))
				fo.write(bytes(wtimestamp,'UTF-8'))
				fo.close()
			except Exception as e:
				raise e
		else:
			print ("File is greater than 1 MB")

f_name = "text"
r_file = readFile()
r_file.fileProperties(f_name)