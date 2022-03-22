import json# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json
import time

filename='yelp_academic_dataset_business.json'
screenname_list=[]
tweet_file= open(filename, "r")

for line in tweet_file:
    # print('hello')
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())    
        idname=tweet['name']
        city_n=tweet['city']
        l=city_n.lower()
        # b_id=tweet['business_id']
        iddname=idname.replace(' ','-')
        g=iddname.lower()
        fl=g+'-'+l
        if fl not in screenname_list:
            with open('business_names_t.txt', 'a') as f:
                f.write(str(fl))
                f.write("\n")
                screenname_list.append(fl)
    except:
        continue
