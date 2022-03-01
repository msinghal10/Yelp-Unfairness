import json
from bs4 import BeautifulSoup
from urllib.request import Request
import requests
import csv
import os

restUrl='https://www.yelp.com/member_search'

temp = []
def extract_first_data(markup):
	soup = BeautifulSoup(markup, 'html.parser')   
	# finding the tag with the id attribute
	c_name = soup.find_all(class_ = 'user-name')
	c_location = soup.find_all(class_ = 'user-location responsive-hidden-small')
	c_image=soup.find_all('img', attrs={'class': 'photo-box-img'})
	c_friend = soup.find_all(class_ = 'friend-count responsive-small-display-inline-block')
	c_review = soup.find_all(class_ = 'review-count responsive-small-display-inline-block')
	c_userid = soup.find_all('a', attrs={'class': 'user-display-name js-analytics-click'}) 
	for n,l,f,r,u,t in zip(c_name,c_location,c_friend,c_review,c_userid,c_image):
		# print(n.text.strip()," --> ",l.text.strip()," --> ",f.text.strip()," --> ",r.text.strip()," --> ",u['href'].split('=')[-1])
		temp.append({
			"userid" : u['href'].split('=')[-1],
			"userimage" : t['src'],
			"name" : n.text.strip(),
			"location" : l.text.strip(),
			"friends" : f.text.strip(),
			"review" : r.text.strip()
		})

def extract_all_data(markup):
	soup = BeautifulSoup(markup, 'html.parser')   
	# finding the tag with the id attribute
	c_name = soup.find_all(class_ = 'user-name')
	c_image=soup.find_all('img', attrs={'class': 'photo-box-img'})
	c_location = soup.find_all(class_ = 'user-location responsive-hidden-small')
	c_friend = soup.find_all(class_ = 'friend-count responsive-small-display-inline-block')
	c_review = soup.find_all(class_ = 'review-count responsive-small-display-inline-block')
	c_userid = soup.find_all('a', attrs={'class': 'user-display-name js-analytics-click'}) 
	for n,l,f,r,u,t in zip(c_name,c_location,c_friend,c_review,c_userid,c_image):
		# print(n.text.strip()," --> ",l.text.strip()," --> ",f.text.strip()," --> ",r.text.strip()," --> ",u['href'].split('=')[-1])
		temp.append({
			"userid" : u['href'].split('=')[-1],
			"userimage" : t['src'],
			"name" : n.text.strip(),
			"location" : l.text.strip(),
			"friends" : f.text.strip(),
			"review" : r.text.strip()
		})

def extract_page_number(markup):
	soup = BeautifulSoup(markup, 'html.parser')   
	# finding the tag with the id attribute
	page_number = soup.find_all(class_ = 'page-of-pages arrange_unit arrange_unit--fill')
	for p in page_number:
		# print(n.text.strip()," --> ",l.text.strip()," --> ",f.text.strip()," --> ",r.text.strip()," --> ",u['href'].split('=')[-1])
		return p.text.strip().split(" ")[-1]

headers = {'Host': 'www.yelp.com',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15',
    'Accept': 'text/json',
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

def data_query(page_number,q_name,q_state,q_city):
	return {'csrftok':'9447e231343a3f537ed3211585ac9d1924628061e43ae34f7ea2c8da21cd4310',
	'start':''+str(page_number)+'',
	'query':''+q_name+'',
	'action_search':'Search',
	'find_loc':''+q_state+':'+q_city+'::'}

def initial_data_query(q_name,q_state,q_city):
	return {'csrftok':'9447e231343a3f537ed3211585ac9d1924628061e43ae34f7ea2c8da21cd4310',
	'query':''+q_name+'',
	'action_search':'Search',
	'find_loc':''+q_state+':'+q_city+'::'}

def initial_check(q_name,q_state,q_city):
	check = requests.post('https://www.yelp.com/member_search', data=initial_data_query(q_name,q_state,q_city), headers=headers)
	out = check.text
	print("Reading Page 1")
	extract_first_data(out)
	#extract the page numbers
	total_page = extract_page_number(out)
	print("Total page numbers: ",total_page)
	if total_page == None:
		total_page = 0
	#calculation for getting the start page value
	c_page = (int(total_page) * 10) - 10
	for i in range(10,c_page,10):
		print("Reading Page: ",(i/10 + 1))
		check = requests.post('https://www.yelp.com/member_search', data=data_query(i,q_name,q_state,q_city), headers=headers)
		out = check.text
		extract_all_data(out)

def write_jsonfile(name,state,city):
	print('Writing the file')
	temp_filename = "search/"+name+"_"+state+"_"+city+".json"
	final = json.dumps(temp, indent=2)
	if os.path.exists(temp_filename):
		os.remove(temp_filename)
	current_directory = os.getcwd()
	final_directory = os.path.join(current_directory, r'search')
	if not os.path.exists(final_directory):
		os.makedirs(final_directory)
	file = open(temp_filename,"w")
	file.write(final)
	file.close()
	temp.clear()

#read.csv file 
with open("g12.csv", 'r') as file:
	csv_file = csv.DictReader(file)
	for row in csv_file:
		# print(dict(row).get('Name'))
		# print(initial_data_query(dict(row).get('Name'),dict(row).get('State'),dict(row).get('City')))		
		initial_check(dict(row).get('Name'),dict(row).get('State'),dict(row).get('City'))
		write_jsonfile(dict(row).get('Name'),dict(row).get('State'),dict(row).get('City'))