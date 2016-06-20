import os
import sys
from bs4 import BeautifulSoup
import requests
from lxml import html
from gi.repository import Notify
import time
from GUInotify import *

prev1=''
prev2=''

def get_news_from_cnet():
	page=requests.get("http://www.cnet.com/")
	if page.status_code != 200:
		sys.stderr.write('Could not connect to cnet.kindly check your iternet connection')
		page=requests.get("http://www.cnet.com/")
	try:
		soup=BeautifulSoup(page.text,'html.parser')
		a=soup.find_all('a',{'class':'itemLink'})[0]
		global prev1
		link=a['href']
		print link;
		a=a.text.encode('ascii','ignore')
		if str(a) != prev1:
			Notification('http://www.cnet.com'+link,str(a))
			prev1=str(a)

	except:
		sys.stderr.write('Could not connect to cnet.kindly check your iternet connection')


def get_news_from_techcrunch():
	page=requests.get("https://techcrunch.com/")
	if page.status_code == 404:
		sys.stderr.write('Could not connect to techcrunch.kindly check your iternet connection')
	try:
		soup=BeautifulSoup(page.text,'html.parser')
		a=soup.find_all('h2',{'class':'post-title'})[0].a
		link=a['href']
		print link;
		a=a.text.encode('ascii','ignore')
		global prev2
		if str(a) != prev2:
			Notification(link,str(a))
			prev2=str(a)
	except:
		sys.stderr.write('Could not connect to techcrunch.kindly check your iternet connection')

def main():
	x=NewsSelector()
	c1=x.c1.get()
	c2=x.c2.get()
	while True:
		if c1 == 1:
			get_news_from_techcrunch()
			time.sleep(60)
		if c2 == 1:
			get_news_from_cnet()
			time.sleep(60)
	
if __name__ == "__main__":
	main()



