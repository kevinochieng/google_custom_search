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
import warnings
warnings.simplefilter(action='ignore', category=Warning)
#
def remove_dup_email(x):

      return list(dict.fromkeys(x))

def remove_dup_phone(x):
      return list(dict.fromkeys(x))
    
def remove_dup_address(x):
    
    return list(dict.fromkeys(x))

# def get_address(html):
#         address=re.findall(r".+, .+, .+", html)
#         address2=re.findall(r".+",html)
#         for j in address2:
#             address.append(j)
#         nodup_address = remove_dup_address(address)
#         return nodup_address
def get_address(html):
#         parsed_text = CommonRegex(html)
#         street_addresses=parsed_text.street_addresses
#         email=re.findall(r"(.+\n)+\d{5}.*)", html)
        email=re.findall(r".+ [0-9]{1,4} .+ .+ .+", html)
        email2=re.findall(r".+, .+, [0-9]{1,4}",html)
        for j in email2:
            email.append(j)
        email3=re.findall(r".+, .+, .+|address .*|Address: .*|Address – .*|Office: .*|Address Details .*|Address .*|Address", html)
        for l in email3:
            email.append(l)
# Faure Street, Paarl, 7646
        nodup_email = remove_dup_email(email)
        return nodup_email 
def get_hours_operation(html):
    try:
        
        phone=re.findall(r'Monday .*|Mon –.*|Sat : .*|Sun: .*|Sat – .*|Sun – .*|Monday –.*|Saturday : .*|Sunday: .*|Saturday – .*|Sunday – .*|Monday – Friday: .*|Mon – Fri: .*|Mon - Fri  .*|Saturday  .*|Sunday  .*|Hours: .*|Mon - Fri .*',html) 
        nodup_phone = remove_dup_phone(phone)
        return nodup_phone
    except:
        pass
     

def get_email(html):

        email=re.findall('\w+@\w+\.{1}\w+', html)
        email1 = re.findall("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",html)
        for e in email1:
            email.append(e)
        nodup_email = remove_dup_email(email)
        return nodup_email

def get_phone(html):

        phone = re.findall(r"(\d{2} \d{3,4} \d{3,4})", html)
        phone1= re.findall(r"((?:\d{2,3}|\(\d{2,3}\))?(?:\s|-|\.)?\d{3,4}(?:\s|-|\.)\d{4})",html)
        phone2=re.findall(r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]",html)
        for p in phone1:
             phone.append(p)
        for x in phone2:
            phone.append(x)
        nodup_phone = remove_dup_phone(phone)
        return nodup_phone

Facebook=[]
Twitter=[]
Linkedin=[]
Youtube=[]
Instagram=[]
Github=[]
df=pd.read_csv("get_numbers_AI.csv")[2650:3000]
url=df['website'].to_list()
# url=['https://www.enavant.co.za']#['https://www.harveyworld.co.za']#,'https://barrydavies.co.za','https://viadata.co.za','https://www.effsaa.org','https://infotraceanalytics.com','https://africa118.com/']
for i in url:
    try:

        
        Facebook=[]
        Twitter=[]
        Linkedin=[]
        Youtube=[]
        Instagram=[]
        Github=[]
        
        headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
        request_response = requests.get(i,headers=headers,verify=False)#,headers=headers)
        status_code = request_response.status_code
        if status_code in [200,406,403]:
                
                website='active'
        else:  
            
            website='inactive'
        if status_code ==200:
            
            
            soup = BeautifulSoup(request_response.content, 'html5lib')
            all_links = soup.find_all('a', href = True)
    #         print(f'all links {all_links}')
            for link in all_links:
                
                if 'facebook' in link.attrs['href']:
                    facebook_link=link.attrs['href']
                    Facebook.append(facebook_link)

                else:
                    facebook_link=''

                if 'twitter' in link.attrs['href']:

                    twitter_link=link.attrs['href']
                    Twitter.append(twitter_link)
                else:
                    twitter_link=''

                if 'linkedin' in link.attrs['href']:
                    linkedin_link= link.attrs['href']
                    Linkedin.append(linkedin_link)
                else:
                    linkedin_link=''
                if 'youtube' in link.attrs['href']:
                    youtube_link =link.attrs['href']
                    Youtube.append(youtube_link)
                else:
                    youtube_link=''

                if 'instagram' in link.attrs['href']:
                    instagram_link=link.attrs['href']
                    Instagram.append(instagram_link)
                else:
                    instagram_link=''
                if 'github' in link.attrs['href']:
                    github_link=link.attrs['href']
                    Github.append(github_link)

                else:
                    github_link=''

            emails_home = get_email(soup.get_text())
            phones_home = get_phone(soup.get_text())
            address_home=get_address(soup.get_text())
            emails_f = emails_home
            phones_f = phones_home  
            # address_f=address_home
            
            lnks=[]
            titles=[]
            non_google_maps=[]
            urls_google2=[]
            urls2 = []
            try:
                non_google_map=soup.find('div',class_='sqs-block map-block sqs-block-map sized vsize-12')['data-block-json']
                non_google_maps.append(non_google_map)
            except:  
                pass
            
            for lnk2 in soup.find_all('a'):

                try:
                    lnk_data=lnk2.get('href')
                    urls2.append(lnk_data)
                    urls_google2=[k for k in urls2 if 'https://www.google.com/maps' in k]
                    
                    
                except:
                    pass
                try:
                    
                    info= soup.find_all('iframe')
                    for j in info:
                        try:  
                            lnk=j['src']
                            lnks.append(lnk)
    #                         print(lnks)

                        except:
                            pass
                    try:  
                        title=j['title']
                        titles.append(title)
                    except:
                        pass
                except:
                    pass
                try:     
                    urls_google=[j for j in lnks if 'https://www.google.com/maps/embed?pb' in j] 
    #                 print(f"urls obtained from nornal google maps{urls_google}")
                except:
                    urls_google=''

            for lnks_ in all_links:
                
    #             print(lnks_)
                
                if 'contact' in lnks_.attrs['href'] or 'Contact' in lnks_.attrs['href'] or 'contactUs' in lnks_.attrs['href']:
                
    
                    contact_lnks=lnks_.attrs['href']
    #                 print(f'contact liks{contact_lnks}')
                    
                    if i in contact_lnks:
                        
                        
                        use_contact_links=contact_lnks
                    else:
                        use_contact_links=i + '/'+ contact_lnks
    #                 print(f"use_contact_links is : {use_contact_links}")
                
                    res_contact = requests.get(use_contact_links,verify=False,headers=headers)
    #                 contact_info = BeautifulSoup(res_contact.text, 'lxml').get_text()
                    contact_info=BeautifulSoup(res_contact.content, 'html5lib')
    #                 print(f'contact info from contact us page url: {contact_info}')
    #                 print('searched contact url:', res_contact.url)
                    # extract contact data
                    emails_contact = get_email(contact_info.get_text())
    #                 print(f'email contact{emails_contact}')
                    phones_contact = get_phone(contact_info.get_text())
                    # address_contact=get_address(contact_info.get_text())
    #                 print(f'phones_contact{phones_contact}')
                    #combining email contacts and email home into a single list
                    emails_f = emails_home
                    for ele1 in emails_contact:
                        emails_f.append(ele1)
                    #combining phone contacts and phone contacts into a single list
                    phones_f = phones_home
                    for ele2 in phones_contact:
                        phones_f.append(ele2)
                    # for ele3 in address_contact:
                    #     address_f.append(ele3)
                        
                    lnks2=[]
                    titles2=[]
                    non_google_maps2=[]
                    urls2_1 = []
                    urls_google2_=[]
                    
                    try:
                        non_google_map1=contact_info.find('div',class_='sqs-block map-block sqs-block-map sized vsize-12')['data-block-json']
                        non_google_maps2.append(non_google_map1)
                    except:  
                        non_google_map1=''
    #                     pass
                    try:
                        all_As_2=contact_info.find_all('a',href = True)
                        for lnk2_ in all_As_2:
                            
                            try:
                                lnk_data1=lnk2_.get('href')
                                urls2_1.append(lnk_data1)
    #                             print(f'check of urls-google_2 is there:{urls2_1}')
                                urls_google2=[l for l in urls2_1 if 'https://www.google.com/maps' in l]
    #                             urls_google2_.append(urls_google2_1)
        
                            except:
                                urls_google2_=''
    #                             pass
                    except:
                        pass
                            
                    try:

                        info1= contact_info.find_all('iframe')
    #                     print(f"all iframes: {info1}")
                        for k in info1:
                            try:  
                                lnki=k['src']
                                lnks2.append(lnki)
    #                             print(lnks)

                            except:
                                pass
                        try:  
                            title1=k['title']
                            titles2.append(title1)
                        except:
                            pass
                    except:
                        pass
                    try:     
                        urls_google1=[m for m in lnks2 if 'https://www.google.com/maps/embed?pb' in m] 
    #                     print(f"urls obtained from nornal google maps{urls_google1}")
                    except:
                        urls_google1=''

            contacts_f = {'url_used':i,'website':'','status_code':'','Facebook':'','Twitter':'','Linkedin':'','Youtube':'','Instagram':'','Github':'','Email':'','Phone':'','urls_google2':'','titles':'','urls_google':'','non_google_maps':'',
                        'titles2':'','urls_google2_':'','non_google_maps2':'','urls_google1':''}
            contacts_f['website']= website
            contacts_f['status_code']= status_code 
            contacts_f['Facebook']= Facebook
            contacts_f['Twitter']= Twitter
            contacts_f['Linkedin']= Linkedin
            contacts_f['Youtube']= Youtube
            contacts_f['Instagram']= Instagram
            contacts_f['Github']= Github
            contacts_f['Email']= emails_f
            contacts_f['Phone']= phones_f 
            # contacts_f['address']= address_f 
            
            contacts_f['urls_google2']= urls_google2
            contacts_f['titles']= titles
            contacts_f['urls_google']= urls_google
            contacts_f['non_google_maps']= non_google_maps
            contacts_f['titles2']= titles2
            contacts_f['urls_google2_']= urls_google2_
            contacts_f['non_google_maps2']= non_google_maps2
            contacts_f['urls_google1']= urls_google1
    #         print(contacts_f)
            print('\n', json.dumps(contacts_f, indent=2))
            with open('get_numbers_AI_2_1_2e.csv', 'a') as f:
                #creater csv writer object
                writer = csv.DictWriter(f, fieldnames=contacts_f.keys())
                writer.writeheader()
                #append rows to the csv
                writer.writerow(contacts_f)
    except:
        pass
