#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests as r
import time
import json
import pandas as pd
import datetime as dt
from datetime import datetime
from pandas.io.json import json_normalize


# In[2]:


#file path
path = 'C:/Users/ACBS-QLRR/Downloads/pythontest/'


# In[3]:


#url to post
action_postURL = 'https://services.bullionstar.com/spot-chart/getChart'
# use get to pull cookies information
res = r.get(action_postURL)


# In[4]:


cleaned_gold = "gold_clean.csv"


# In[5]:





# In[6]:


res.status_code
res.headers['content-type']
res.encoding
res.text
res.content
time.sleep(5)
res.cookies


# In[7]:


#Get the Cookies
search_cookies = res.cookies


# In[9]:


#post method data
post_data = {'method':'POST',"product":"false","productId":"0","productTo":"false","productIdTo":"0",
             "fromIndex":"XAU" ,"toIndex":"USD","period":"CUSTOM",
             "width":"600", "height":"300","timeZoneId": "Asia/Saigon","weightUnit":"tr_oz","fromDateString":"01-01-2000 00:00","toDateString":"02-12-2021 00:00"}


# In[10]:


#headers information
headers = {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}


# In[11]:


#request post data
res_post = r.post(action_postURL, data=post_data, cookies=search_cookies, headers = headers)


# In[12]:


#pull data into  json format
values = res_post.json()


# In[13]:


#normalize data with Brazilian gold values 
gold_values = res_post.json()["dataSeries"]
df = json_normalize(gold_values)


# In[14]:


df.to_csv(path+"gold_clean.csv", mode='a', header=False,index=False)


# In[15]:


print("a")


# In[ ]:


https://sdbullion.com/gold-prices-2000


# In[132]:


# Library for opening url and creating 
# requests
import urllib.request


# In[133]:


# pretty-print python data structures
from pprint import pprint

# for parsing all the tables present 
# on the website
from html_table_parser.parser import HTMLTableParser

# for converting the parsed data in a
# pandas dataframe
import pandas as pd


# In[134]:


# Opens a website and read its
# binary contents (HTTP Response Body)
def url_get_contents(url):

    # Opens a website and read its
    # binary contents (HTTP Response Body)

    #making request to the website
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)

    #reading contents of the website
    return f.read()


# In[66]:





# In[135]:


lin2=[]
lin=[]
for g in range(2000,2022):
    lk="https://sdbullion.com/gold-prices-"+str(g)
    lin.append(lk)


# In[136]:



for url2 in lin:
    print(url2)
    # defining the html contents of a URL.
    #xhtml = url_get_contents('https://s.cafef.vn/TraCuuLichSu2/1/HOSE/26/11/2021.chn').decode('utf-8')
    xhtml = url_get_contents(url2).decode('utf-8')
    # Defining the HTMLTableParser object
    p = HTMLTableParser()

    # feeding the html contents in the
    # HTMLTableParser object
    p.feed(xhtml)

    # Now finally obtaining the data of
    # the table required
    p2=p.tables[0]

    p3=pd.DataFrame(p2)
    p3b=p3
    p3b.columns = ["Date","Gold AM","Gold PM"] 
    p3b = p3b[1:]
    #p3["Date"]=url2[-14:][:10]
    #p3
    #p3b = p3.rename(columns = {0:'Ma',1:'Giadongcua',3:'Thaydoi',5:'Giathamchieu',6:'Giamocua',7:'Giacaonhat',8:'Giathapnhat',9:'KLGDkhoplenh',10:'GTGDkhoplenh',11:'KLGDthoathuan',12:'GTGDthoathuan'})
    lin2.append(p3b)
    #p3.to_excel("‪giaCk"+str(i)+".xlsx")  


# In[138]:


lin2[0]


# In[137]:


lin2[19]


# In[72]:


lin2[19]


# In[139]:


final_data_day = pd.concat(lin2)
final_data_day


# In[140]:


final_data_day.to_excel(path+"gold2000to2019.xlsx")  


# In[ ]:





# In[ ]:





# In[112]:





# In[ ]:





# In[114]:





# In[ ]:





# In[ ]:





# In[ ]:


https://www.usagold.com/daily-gold-price-history/


# In[ ]:





# In[82]:


lin2=[]
lin=[]

lk="https://www.usagold.com/daily-gold-price-history/"
lin.append(lk)


# In[83]:


for url2 in lin:
    print(url2)
    # defining the html contents of a URL.
    #xhtml = url_get_contents('https://s.cafef.vn/TraCuuLichSu2/1/HOSE/26/11/2021.chn').decode('utf-8')
    xhtml = url_get_contents(url2).decode('utf-8')
    # Defining the HTMLTableParser object
    p = HTMLTableParser()

    # feeding the html contents in the
    # HTMLTableParser object
    p.feed(xhtml)

    # Now finally obtaining the data of
    # the table required
    p2=p.tables[0]
    p2
    #p3["Date"]=url2[-14:][:10]
    #p3
    #p3b = p3.rename(columns = {0:'Ma',1:'Giadongcua',3:'Thaydoi',5:'Giathamchieu',6:'Giamocua',7:'Giacaonhat',8:'Giathapnhat',9:'KLGDkhoplenh',10:'GTGDkhoplenh',11:'KLGDthoathuan',12:'GTGDthoathuan'})
    lin2.append(p3b)
    #p3.to_excel("‪giaCk"+str(i)+".xlsx")  


# In[84]:


p2


# In[ ]:





# In[ ]:





# In[ ]:





# In[120]:





# In[ ]:





# In[122]:





# In[ ]:


https://www.investing.com/commodities/crude-oil-historical-data


# In[123]:


# Library for opening url and creating 
# requests
import urllib.request
# pretty-print python data structures
from pprint import pprint

# for parsing all the tables present 
# on the website
from html_table_parser.parser import HTMLTableParser

# for converting the parsed data in a
# pandas dataframe
import pandas as pd

# Opens a website and read its
# binary contents (HTTP Response Body)
def url_get_contents(url):

    # Opens a website and read its
    # binary contents (HTTP Response Body)

    #making request to the website
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)

    #reading contents of the website
    return f.read()

lin2=[]


# In[128]:


site2="https://www.investing.com/commodities/crude-oil-historical-data"


# In[129]:


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

site= site2
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page)
print(soup)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[161]:





# In[165]:


dfr2=[]
for i in range(2000,2022):
    site4="https://www.usagold.com/daily-gold-price-history/?ddYears="+str(i)
    from bs4 import BeautifulSoup
    from urllib.request import Request, urlopen

    site= site4
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page)
    print(soup)


    for item in soup.find_all('table',{"id":"pricehistorytable"}):
        aa=item.select("td",{'align':"left"})
        print(aa)
        
    for a in aa:
        dfr2.append(a.text)


    


# In[166]:


df_1=pd.DataFrame(dfr2)
df_1    


# In[167]:


df_1.to_excel(path+"golddata.xlsx")    


# In[ ]:




