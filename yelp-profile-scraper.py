from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import pandas as pd
import requests
import urllib
import csv
import re
import time
of_folder='profiles/'
def html_parse(restUrl,username):
	since-loca = []
	follow = []
	revNum = []
	revStars = []
	revDate = []
	revName = []
	name_bus=[]
	pages=[]
	userImage=[]
	mylist=[]
	headers = {'Host': 'www.yelp.com',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:96.0) Gecko/20100101 Firefox/96.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'Referer': 'https://www.yelp.com/biz/babes-chicken-dinner-house-arlington',
	'Connection': 'keep-alive',
	'Cookie': 'hl=en_US; _ga=GA1.2.5199E242AE7A9828; wdi=1|5199E242AE7A9828|0x1.85cd45d77547ep+30|750552dedf1a5b33; OptanonConsent=isIABGlobal=false&datestamp=Tue+Jan+25+2022+14%3A25%3A03+GMT-0600+(Central+Standard+Time)&version=6.10.0&hosts=&consentId=c8048ce3-8edf-46ae-95e3-453941167af7&interactionCount=1&landingPath=NotLandingPage&groups=BG10%3A1%2CC0003%3A1%2CC0002%3A1%2CC0001%3A1%2CC0004%3A1&AwaitingReconsent=false; xcj=1|vQ6dCM7O5xkUVrdu7J8SgO8kH6NoNKlTZ052sM8iksk; _fbp=fb.1.1634947322641.106904531; __qca=P0-1019874423-1634947322835; __adroll_fpc=266ac75b13c6fb74ddaa04ca3f0e7610-1634947328852; __ar_v4=7YODZSYLRVB65MFGKXSHSA%3A20220124%3A1%7C7YX6SJQ4RZAMPB6LZ7CHFF%3A20220105%3A22%7CBHPKS4B4ONEJJMGH4QCJZR%3A20220105%3A25%7CQB5JPFIKRZDSBOZSULG4YB%3A20220105%3A25%7CQAR3DEYXR5AFJIPXF5PVR4%3A20220105%3A2; location=%7B%22city%22%3A+%22Arlington%22%2C+%22state%22%3A+%22TX%22%2C+%22country%22%3A+%22US%22%2C+%22latitude%22%3A+32.735949939078246%2C+%22longitude%22%3A+-97.10804452636717%2C+%22max_latitude%22%3A+32.787698%2C+%22min_latitude%22%3A+32.633367%2C+%22max_longitude%22%3A+-97.046431%2C+%22min_longitude%22%3A+-97.193004%2C+%22zip%22%3A+%22%22%2C+%22address1%22%3A+%22%22%2C+%22address2%22%3A+%22%22%2C+%22address3%22%3A+null%2C+%22neighborhood%22%3A+null%2C+%22borough%22%3A+null%2C+%22provenance%22%3A+%22YELP_GEOCODING_ENGINE%22%2C+%22display%22%3A+%22Arlington%2C+TX%22%2C+%22unformatted%22%3A+%22Arlington%2C+TX%22%2C+%22isGoogleHood%22%3A+null%2C+%22usingDefaultZip%22%3A+null%2C+%22accuracy%22%3A+4.0%2C+%22language%22%3A+null%7D; g_state={"i_p":1637702854821,"i_l":2}; G_ENABLED_IDPS=google; zs=GHBmkTCiKG9yfIT88A2zhQsPhSidYQ; zss=J5XaY1_jJQFRwAFFdSKCJ1TMhSidYQ; hsfd=0; _clck=11xfkk1|1|eyf|0; qntcst=D; _gid=GA1.2.1794528002.1643049056; _gcl_au=1.1.697792570.1643049130; _ga_5GWWL7FDT0=GS1.1.1643049130.1.0.1643049165.25; _clsk=mhccuj|1643142299403|4|0|h.clarity.ms/collect; bse=2ef9525ac1ba4e84a650b7d00861b890; pid=295592b94ff8170b; _uetsid=f26645907d4311ecbadf23f20c6c0be1; _uetvid=749002e0339411ec9c8901156f378aa7',
	'Upgrade-Insecure-Requests': '1',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-User': '?1',
	'Cache-Control': 'max-age=0'}
	html = requests.get(restUrl,headers=headers)

	soup = BeautifulSoup(html.text, "html.parser")


	for iterReviews in soup.find_all('ul',{'class':'ylist'}):
		sl = iterReviews.find('li')
		sl = str(sl).replace('<p>', '')
		sl = str(sl).replace('</p>', '')
		since-loca.append(sl)


	for iterFrndCnt in soup.find_all('ul',{'class':'ylist ylist--condensed'}):
		eachFrndCnt = iterFrndCnt.find('li')
		eachFrndCnt = str(eachFrndCnt).replace('<strong>', '')
		eachFrndCnt = str(eachFrndCnt).replace('</strong>', '')
		follow.append(eachFrndCnt)

	for iterRevCnt in soup.find_all('li',{'class':'review-count responsive-small-display-inline-block'}):
		eachRevCnt = iterRevCnt.find('b')
		eachRevCnt = str(eachRevCnt).replace('<b>', '')
		eachRevCnt = str(eachRevCnt).replace('</b>', '')
		revNum.append(eachRevCnt)

	for iterDate in soup.find_all('span',{'class':'rating-qualifier'}):
		eachDate = str(iterDate)[40:50]
		eachDate = str(eachDate).replace('\n', '')
		eachDate = str(eachDate).replace(' ', '')
		revDate.append(eachDate)

	
	wrCsv = pd.DataFrame(list(zip(*[review, frndCnt, revNum, revDate, revName, revStars,userImage]))).add_prefix('Col')
	with open(of_folder+username+".csv", 'a') as f:
		wrCsv.to_csv(f, header=False,index = False)
	# return my_list
def main():
	h=[]
	jj=[]
	listofindex=["Review","Friends Count","Review Count","Review Date","User Name","Rating","User Image"]
	f = open('g1.txt', 'r')
	for line in f:
		dat = line
		dat1 = dat.replace('\n','')
		try:	
			restUrl = 'https://www.yelp.com/user_details?userid='+dat1
			check = requests.get(restUrl)
			if check.status_code == 200:
				print(restUrl)
				with open(of_folder+dat1+".csv", 'w') as file:
					dw = csv.DictWriter(file, delimiter=',', fieldnames=listofindex)
					dw.writeheader()
				html_parse(restUrl,dat1)
			else:
				continue
		except:
			pass
main()







