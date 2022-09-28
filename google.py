# Import the beautifulsoup
# and request libraries of python.
import requests
import bs4
import json
import csv
import time 
import requests
from bs4 import BeautifulSoup
import csv
import json 
from tld import get_tld
import requests
import re
import csv
import json
import pandas as pd
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import numpy as np
from numpy import random
from time import sleep
import requests
from bs4 import BeautifulSoup
import csv
import json 
import requests
from bs4 import BeautifulSoup
import csv
import json 
from tld import get_tld
import requests
import re
import csv
import json
import pandas as pd
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import numpy as np
from numpy import random
from time import sleep
# sleeptime = random.uniform(1,2)
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
context = ssl._create_unverified_context()
# sleeptime = random.uniform(1,2)


df=pd.read_csv("extracted_phones_emails.csv",encoding='latin-1')[14530:]
print(df.shape)
# df.head(3)
text=df['search_terms'].to_list()
# text= ["flutterwave CEO site:linkedin.com","Africa118 CEO site:linkedin.com"]

for i in text:
    # try:    
        url = 'https://www.ask.com/web?q=' + i
        ua = UserAgent()
        userAgent = ua.random
        headers = {'User-Agent': userAgent}
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=2)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        request_result=session.get(url)
        soup = bs4.BeautifulSoup(request_result.text,"html.parser")
        heading=soup.findAll('div',class_='PartialSearchResults-item-title')
        description=soup.findAll('div',class_='PartialSearchResults-item-right-block')
        contact_f={'url_used':i,'url':'','title':'','desc':''}
        for i in heading:
            
            url=i.find('a')['href']
            title=i.find('a').text
    #         desc=j.text        
            contact_f['url']=url
            contact_f['title']=title

            print('\n', json.dumps(contact_f, indent=2))
            with open('jouner4.csv', 'a',encoding='utf-8') as f:

                writer = csv.DictWriter(f, fieldnames=contact_f.keys())
                # writer.writeheader()
                #append rows to the csv
                writer.writerow(contact_f)
            sleeptime = random.uniform(5,10)

    # except:
    #     print("pass this search term")
    #     pass
