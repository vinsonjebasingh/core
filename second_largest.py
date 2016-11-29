#Write a program to implement a method which takes a list as an argument and returns second largest number.
#read from standard input and write to standard output.
class Secondlargest:
	# Method 1
	def secLargestMthdone(self, list_arr):
		n = len(list_arr)
		list_arr.sort()														
		print ('Second largest : ', list_arr[n-2])
	# Method 2
	def findSecLargest(self, list_arr):
		f_largest = list_arr[0]
		s_largest = list_arr[0]
		for i in range(len(list_arr)):
			if list_arr[i] > f_largest:
				s_largest = f_largest
				f_largest = list_arr[i]
			elif list_arr[i] > s_largest:
				s_largest = list_arr[i]
		print ('Second largest : ', s_largest) 

list_arr = [-5,3,12,9,-17,21,16]
s_large = Secondlargest()
s_large.secLargestMthdone(list_arr) #Method 1
s_large.findSecLargest(list_arr) #Method 2



