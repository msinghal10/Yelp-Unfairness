from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import pandas as pd
import requests
import urllib
import csv
import re
import time
of_folder='data/'
def html_parse(restUrl,businessname):
	review = []
	frndCnt = []
	revNum = []
	revStars = []
	revDate = []
	revName = []
	revplace=[]
	name_bus=[]
	pages=[]
	userImage=[]
	mylist=[]
	# Change the cookies of the header, each time you start the code.
	headers = {'Host': 'www.yelp.com',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:96.0) Gecko/20100101 Firefox/96.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'Referer': 'https://www.yelp.com/biz/babes-chicken-dinner-house-arlington',
	'Connection': 'keep-alive',
	'Cookie': 'location=%7B%22city%22%3A+%22Arlington%22%2C+%22state%22%3A+%22TX%22%2C+%22country%22%3A+%22US%22%2C+%22latitude%22%3A+32.735949939078246%2C+%22longitude%22%3A+-97.10804452636717%2C+%22max_latitude%22%3A+32.787698%2C+%22min_latitude%22%3A+32.633367%2C+%22max_longitude%22%3A+-97.046431%2C+%22min_longitude%22%3A+-97.193004%2C+%22zip%22%3A+%22%22%2C+%22address1%22%3A+%22%22%2C+%22address2%22%3A+%22%22%2C+%22address3%22%3A+null%2C+%22neighborhood%22%3A+null%2C+%22borough%22%3A+null%2C+%22provenance%22%3A+%22YELP_GEOCODING_ENGINE%22%2C+%22display%22%3A+%22Arlington%2C+TX%22%2C+%22unformatted%22%3A+%22Arlington%2C+TX%22%2C+%22isGoogleHood%22%3A+null%2C+%22usingDefaultZip%22%3A+null%2C+%22accuracy%22%3A+4.0%2C+%22language%22%3A+null%7D; hl=en_US; wdi=1|074C9D39FB9D3030|0x1.8a4c7aa035c74p+30|0e02339f8f47ee66; xcj=1|FZLQ4LWbaVj16JK0vGR_KdY1amXpgIMKbm-hD_99nI8; _ga=GA1.2.074C9D39FB9D3030; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+17+2022+15%3A41%3A30+GMT%2B0530+(India+Standard+Time)&version=6.34.0&hosts=&consentId=0afa044a-61ac-43a4-b6cb-ac083cb80861&interactionCount=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0002%3A1%2CC0001%3A1%2CC0004%3A1%2CBG40%3A1&AwaitingReconsent=false&isGpcEnabled=0; __qca=P0-245944813-1641321769732; __adroll_fpc=e571db94111ecf4acd659df7506a17ef-1641321770400; __ar_v4=%7CBHPKS4B4ONEJJMGH4QCJZR%3A20220431%3A1%7CQB5JPFIKRZDSBOZSULG4YB%3A20220431%3A1%7C7YX6SJQ4RZAMPB6LZ7CHFF%3A20220431%3A1; _clck=1d8mcd|1|f25|0; _gcl_au=1.1.123541649.1651385235; _fbp=fb.1.1651385238172.1782538474; G_ENABLED_IDPS=google; _tt_enable_cookie=1; _ttp=1c53e490-7fd4-478b-8c4e-629277b2e8f0; zs=0xo4H7b5BVHMsIAeNGzhlZBMo72RYg; zss=epnEQ4yagE06xTLejnF36E8oo72RYg; uuac=NgSrlf-frzQoUUkj1joyyL8hhbTs4jio1p-SJJoulVM; _uetvid=1d7f19c06d8e11eca230515ee5bcd359; bse=c034339cf55d4b0ca3eeb4eeec9a7045; pid=d8b9c679071bdd2b; _gid=GA1.2.1801390908.1655460692; _gat_www=1; _gat_global=1',
	'Upgrade-Insecure-Requests': '1',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-User': '?1',
	'Cache-Control': 'max-age=0'}
	html = requests.get(restUrl,headers=headers)

	soup = BeautifulSoup(html.text, "html.parser")

	for iterReviews in soup.find_all('div',{'class':'review-content'}):
		eachReview = iterReviews.find('p')
		eachReview = str(eachReview).replace('<br>', '')
		eachReview = str(eachReview).replace('<br/>', '')
		eachReview = eachReview[13:-4]
		review.append(eachReview)

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

	for iterDate in soup.find_all('span',{'class':'rating-qualifier'}):
		eachDate = str(iterDate)[40:50]
		eachDate = str(eachDate).replace('\n', '')
		eachDate = str(eachDate).replace(' ', '')
		revDate.append(eachDate)

	for iterName in soup.find_all('li',{'class':'user-name'}):
		eachName = iterName.find('span')
		eachName = str(eachName)[75:100]
		eachName = eachName.split('<')[0]
		revName.append(eachName)

	for iterRevplc in soup.find_all('li',{'class':'user-location responsive-hidden-small'}):
		eachRevplc = iterRevplc.find('b')
		eachRevplc = str(eachRevplc).replace('<b>', '')
		eachRevplc = str(eachRevplc).replace('</b>', '')
		revplace.append(eachRevplc)

	for iterStars in soup.find_all('div',{'class':'biz-rating__stars'}):
		eachStars = iterStars.find('img')
		eachStars = str(eachStars)[10:25]
		eachStars =eachStars.replace('star rating','')
		eachStars=eachStars.replace('.0','')
		revStars.append(eachStars)

	for iterimage in soup.find_all('div',{'class':'photo-box pb-60s'}):
		eachimage = iterimage.find('img')
		userImage.append(eachimage['src'])

	for iterpage in soup.find_all('div',{'class':'arrange arrange--stack arrange--baseline arrange--6'}):
		page = iterpage.find('div')
		page = str(page)[73:80]
		pages.append(page)
		my_list = [x.split()[2] for x in pages]
		my_list.append(my_list)
	

	wrCsv = pd.DataFrame(list(zip(*[review, frndCnt, revNum, revDate, revName,revplace,revStars,userImage]))).add_prefix('Col')

	with open(of_folder+businessname+".csv", 'a+') as f:
		wrCsv.to_csv(f, header=False,index = False)

	return my_list
	
def main():
	h=[]
	jj=[]
	listofindex=["Review","Friends Count","Review Count","Review Date","User Name","Location","Rating","User Image"]
	f = open('batch-newadd.txt', 'r')
	for line in f:
		dat = line
		dat1 = dat.replace('\n','')
		try:
			time.sleep(4)	
			restUrl = 'https://www.yelp.com/not_recommended_reviews/'+dat1
			check = requests.get(restUrl)
			if check.status_code == 200:
				print(restUrl)
				with open(of_folder+dat1+".csv", 'w') as file:
					dw = csv.DictWriter(file, delimiter=',', fieldnames=listofindex)
					dw.writeheader()
				h=html_parse(restUrl,dat1)
				j=h[0]
				j=int(j)
				next_page = 10
				k=(j-1)*10
				print(k)
				while next_page <= k:
					restUrl='https://www.yelp.com/not_recommended_reviews/'+dat1+'?not_recommended_start='+str(next_page)
					check = requests.get(restUrl)
					print(restUrl)
					time.sleep(5)
					jj=html_parse(restUrl,dat1)
					next_page += 10
			else:
				continue
		except:
			with open('not-fount.txt','a') as file:
				file.write(str(dat1))
				file.write('\n')
			pass
main()







