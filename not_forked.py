#write a program to list all the repos from given url which is not forked i.e. "fork" = False.
#https://api.github.com/users/mralexgray/repos

import urllib.request
import json
import pprint

class forkUrl:
	def getForkedfalseUrl(self, url):
		req = urllib.request.Request(url)
		res = urllib.request.urlopen(req)
		responseData = res.read().decode('utf-8')
		res_jsonObj = json.loads(responseData)
		for i in res_jsonObj:
			if(i['fork'] == False):
				print (i['url'])

url = "https://api.github.com/users/mralexgray/repos"
f = forkUrl()
f.getForkedfalseUrl(url)