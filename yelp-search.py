from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import pandas as pd
import requests
import urllib
import csv
import re
import time
of_folder='search/'
def html_parse(restUrl,userss,state,city):
	review = []
	frndCnt = []
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
	'Referer': 'https://www.yelp.com/member_search',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Content-Length': '141',
	'Origin': 'https://www.yelp.com',
	'Connection': 'keep-alive',
	'Cookie': 'hl=en_US; _ga=GA1.2.CD63542C26D8BAD3; wdi=1|CD63542C26D8BAD3|0x1.880631bb33bacp+30|51642f92a5ec89bd; OptanonConsent=isIABGlobal=false&datestamp=Tue+Feb+08+2022+16%3A18%3A23+GMT-0600+(Central+Standard+Time)&version=6.10.0&hosts=&consentId=c8048ce3-8edf-46ae-95e3-453941167af7&interactionCount=1&landingPath=NotLandingPage&groups=BG10%3A1%2CC0003%3A1%2CC0002%3A1%2CC0001%3A1%2CC0004%3A1&AwaitingReconsent=false; xcj=1|_AZWkP4p7lyvAqcoctDLNcePb4P95DuOZRENIB_mvE4; _fbp=fb.1.1634947322641.106904531; __qca=P0-1019874423-1634947322835; __adroll_fpc=266ac75b13c6fb74ddaa04ca3f0e7610-1634947328852; __ar_v4=QAR3DEYXR5AFJIPXF5PVR4%3A20220209%3A2%7C7YX6SJQ4RZAMPB6LZ7CHFF%3A20220209%3A4%7CQB5JPFIKRZDSBOZSULG4YB%3A20220209%3A8%7CBHPKS4B4ONEJJMGH4QCJZR%3A20220209%3A8%7C7YODZSYLRVB65MFGKXSHSA%3A20220124%3A5; location=%7B%22city%22%3A+%22Arlington%22%2C+%22county%22%3A+%22Tarrant+County%22%2C+%22state%22%3A+%22TX%22%2C+%22location_type%22%3A+%22locality%22%2C+%22address1%22%3A+%22%22%2C+%22latitude%22%3A+32.735949939078246%2C+%22min_longitude%22%3A+-97.193004%2C+%22unformatted%22%3A+%22Arlington%2C+TX%22%2C+%22address2%22%3A+%22%22%2C+%22longitude%22%3A+-97.10804452636717%2C+%22max_longitude%22%3A+-97.046431%2C+%22display%22%3A+%22Arlington%2C+TX%22%2C+%22max_latitude%22%3A+32.787698%2C+%22min_latitude%22%3A+32.633367%2C+%22accuracy%22%3A+4%2C+%22provenance%22%3A+%22YELP_GEOCODING_ENGINE%22%2C+%22place_id%22%3A+%221542%22%2C+%22country%22%3A+%22US%22%2C+%22zip%22%3A+%22%22%2C+%22parent_id%22%3A+%22PDxXVGTwT_Jc9hsRkox67Q%22%2C+%22address3%22%3A+%22%22%2C+%22borough%22%3A+%22%22%2C+%22isGoogleHood%22%3A+false%2C+%22language%22%3A+null%2C+%22neighborhood%22%3A+%22%22%2C+%22polygons%22%3A+null%2C+%22usingDefaultZip%22%3A+false%2C+%22confident%22%3A+null%2C+%22place_key%22%3A+%22TX%3AArlington%3A%3A%22%7D; g_state={"i_p":1637702854821,"i_l":2}; G_ENABLED_IDPS=google; zs=GHBmkTCiKG9yfIT88A2zhQsPhSidYQ; zss=J5XaY1_jJQFRwAFFdSKCJ1TMhSidYQ; hsfd=0; _clck=11xfkk1|1|eys|0; _gcl_au=1.1.697792570.1643049130; _ga_5GWWL7FDT0=GS1.1.1643049130.1.0.1643049165.25; _gid=GA1.2.1198644622.1644258059; _uetvid=749002e0339411ec9c8901156f378aa7; bse=95955728b25a4c6381766ab49e80a102; pid=17056b09066326b1; recentlocations=; _gat_www=1; _gat_global=1',
	'Upgrade-Insecure-Requests': '1',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-User':'?1',
	'TE': 'trailers'}
	dt={'csrftok=9447e231343a3f537ed3211585ac9d1924628061e43ae34f7ea2c8da21cd4310&start=0&query='+userss+'&find_loc='+state+'%3A'+city+'%3A%3A'}
	html = requests.get(restUrl,data=dt,headers=headers)

	soup = BeautifulSoup(html.text, "html.parser")

	for iterFrndCnt in soup.find_all('li',{'class':'friend-count responsive-small-display-inline-block'}):
		eachFrndCnt = iterFrndCnt.find('b')
		eachFrndCnt = str(eachFrndCnt).replace('<b>', '')
		eachFrndCnt = str(eachFrndCnt).replace('</b>', '')
		frndCnt.append(eachFrndCnt)

	for iterRevCnt in soup.find_all('li',{'class':'review-count responsive-small-display-inline-block'}):
		eachRevCnt = iterRevCnt.find('b')
		eachRevCnt = str(eachRevCnt).replace('<b>', '')
		eachRevCnt = str(eachRevCnt).replace('</b>', '')
		revNum.append(eachRevCnt)

	for iterName in soup.find_all('li',{'class':'user-name'}):
		eachName = iterName.find('a')
		revName.append(eachName['href'])

	for iterimage in soup.find_all('div',{'class':'photo-box pb-60s'}):
		eachimage = iterimage.find('img')
		userImage.append(eachimage['src'])

	for iterpage in soup.find_all('div',{'class':'arrange arrange--stack arrange--baseline arrange--6'}):
		page = iterpage.find('div')
		page = str(page)[73:80]
		pages.append(page)
		my_list = [x.split()[2] for x in pages]
		my_list.append(my_list)
	

	wrCsv = pd.DataFrame(list(zip(*[frndCnt, revNum, revName, userImage]))).add_prefix('Col')

	with open(of_folder+u+".csv", 'a+') as f:
		wrCsv.to_csv(f, header=False,index = False)
	return my_list


def html_parse1(restUrl,nextpage,userss,state,city):
	review = []
	frndCnt = []
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
	'Referer': 'https://www.yelp.com/member_search',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Content-Length': '141',
	'Origin': 'https://www.yelp.com',
	'Connection': 'keep-alive',
	'Cookie': 'hl=en_US; _ga=GA1.2.CD63542C26D8BAD3; wdi=1|CD63542C26D8BAD3|0x1.880631bb33bacp+30|51642f92a5ec89bd; OptanonConsent=isIABGlobal=false&datestamp=Tue+Feb+08+2022+16%3A18%3A23+GMT-0600+(Central+Standard+Time)&version=6.10.0&hosts=&consentId=c8048ce3-8edf-46ae-95e3-453941167af7&interactionCount=1&landingPath=NotLandingPage&groups=BG10%3A1%2CC0003%3A1%2CC0002%3A1%2CC0001%3A1%2CC0004%3A1&AwaitingReconsent=false; xcj=1|_AZWkP4p7lyvAqcoctDLNcePb4P95DuOZRENIB_mvE4; _fbp=fb.1.1634947322641.106904531; __qca=P0-1019874423-1634947322835; __adroll_fpc=266ac75b13c6fb74ddaa04ca3f0e7610-1634947328852; __ar_v4=QAR3DEYXR5AFJIPXF5PVR4%3A20220209%3A2%7C7YX6SJQ4RZAMPB6LZ7CHFF%3A20220209%3A4%7CQB5JPFIKRZDSBOZSULG4YB%3A20220209%3A8%7CBHPKS4B4ONEJJMGH4QCJZR%3A20220209%3A8%7C7YODZSYLRVB65MFGKXSHSA%3A20220124%3A5; location=%7B%22city%22%3A+%22Arlington%22%2C+%22county%22%3A+%22Tarrant+County%22%2C+%22state%22%3A+%22TX%22%2C+%22location_type%22%3A+%22locality%22%2C+%22address1%22%3A+%22%22%2C+%22latitude%22%3A+32.735949939078246%2C+%22min_longitude%22%3A+-97.193004%2C+%22unformatted%22%3A+%22Arlington%2C+TX%22%2C+%22address2%22%3A+%22%22%2C+%22longitude%22%3A+-97.10804452636717%2C+%22max_longitude%22%3A+-97.046431%2C+%22display%22%3A+%22Arlington%2C+TX%22%2C+%22max_latitude%22%3A+32.787698%2C+%22min_latitude%22%3A+32.633367%2C+%22accuracy%22%3A+4%2C+%22provenance%22%3A+%22YELP_GEOCODING_ENGINE%22%2C+%22place_id%22%3A+%221542%22%2C+%22country%22%3A+%22US%22%2C+%22zip%22%3A+%22%22%2C+%22parent_id%22%3A+%22PDxXVGTwT_Jc9hsRkox67Q%22%2C+%22address3%22%3A+%22%22%2C+%22borough%22%3A+%22%22%2C+%22isGoogleHood%22%3A+false%2C+%22language%22%3A+null%2C+%22neighborhood%22%3A+%22%22%2C+%22polygons%22%3A+null%2C+%22usingDefaultZip%22%3A+false%2C+%22confident%22%3A+null%2C+%22place_key%22%3A+%22TX%3AArlington%3A%3A%22%7D; g_state={"i_p":1637702854821,"i_l":2}; G_ENABLED_IDPS=google; zs=GHBmkTCiKG9yfIT88A2zhQsPhSidYQ; zss=J5XaY1_jJQFRwAFFdSKCJ1TMhSidYQ; hsfd=0; _clck=11xfkk1|1|eys|0; _gcl_au=1.1.697792570.1643049130; _ga_5GWWL7FDT0=GS1.1.1643049130.1.0.1643049165.25; _gid=GA1.2.1198644622.1644258059; _uetvid=749002e0339411ec9c8901156f378aa7; bse=95955728b25a4c6381766ab49e80a102; pid=17056b09066326b1; recentlocations=; _gat_www=1; _gat_global=1',
	'Upgrade-Insecure-Requests': '1',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-User':'?1',
	'TE': 'trailers'}
	dt={'csrftok=9447e231343a3f537ed3211585ac9d1924628061e43ae34f7ea2c8da21cd4310&start='+nextpage+'&query='+userss+'&find_loc='+state+'%3A'+city+'%3A%3A'}
	html = requests.get(restUrl,data=dt,headers=headers)

	soup = BeautifulSoup(html.text, "html.parser")

	for iterFrndCnt in soup.find_all('li',{'class':'friend-count responsive-small-display-inline-block'}):
		eachFrndCnt = iterFrndCnt.find('b')
		eachFrndCnt = str(eachFrndCnt).replace('<b>', '')
		eachFrndCnt = str(eachFrndCnt).replace('</b>', '')
		frndCnt.append(eachFrndCnt)

	for iterRevCnt in soup.find_all('li',{'class':'review-count responsive-small-display-inline-block'}):
		eachRevCnt = iterRevCnt.find('b')
		eachRevCnt = str(eachRevCnt).replace('<b>', '')
		eachRevCnt = str(eachRevCnt).replace('</b>', '')
		revNum.append(eachRevCnt)

	for iterName in soup.find_all('li',{'class':'user-name'}):
		eachName = iterName.find('a')
		revName.append(eachName['href'])

	for iterimage in soup.find_all('div',{'class':'photo-box pb-60s'}):
		eachimage = iterimage.find('img')
		userImage.append(eachimage['src'])

	for iterpage in soup.find_all('div',{'class':'arrange arrange--stack arrange--baseline arrange--6'}):
		page = iterpage.find('div')
		page = str(page)[73:80]
		pages.append(page)
		my_list = [x.split()[2] for x in pages]
		my_list.append(my_list)
	

	wrCsv = pd.DataFrame(list(zip(*[frndCnt, revNum, revName, userImage]))).add_prefix('Col')

	with open(of_folder+u+".csv", 'a+') as f:
		wrCsv.to_csv(f, header=False,index = False)
	return my_list


def main():
	h=[]
	jj=[]
	listofindex=["Friends Count","Review Count","User Name","User Image"]
	df=pd.read_csv('g12.csv')
	# print(df)
	for row in df.itertuples():
		u=row.Name
		g=row.State
		asw=row.City
		print(u)
		try:	
			restUrl = 'https://www.yelp.com/member_search'
			check = requests.get(restUrl)
			print(check)
			if check.status_code == 200:
				print(restUrl)
				with open(of_folder+u+".csv", 'w') as file:
					dw = csv.DictWriter(file, delimiter=',', fieldnames=listofindex)
					dw.writeheader()
				h=html_parse(restUrl,u,g,asw)
				j=h[0]
				j=int(j)
				next_page = 10
				k=(j-1)*10
				print(k)
				while next_page <= k:
					restUrl='https://www.yelp.com/member_search'
					check = requests.get(restUrl)
					print(restUrl)
					time.sleep(2)
					jj=html_parse1(restUrl,str(next_page),u,g,asw)
					next_page += 10
			else:
				continue
		except:
			pass
main()







