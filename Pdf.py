
# coding: utf-8

# In[6]:

import pdfkit as pk


# In[ ]:




# In[7]:

def pdfu(url):
    filename = url.split("?")[0].split("/")[-1]
    pk.from_url(url,"./buk/"+filename+".pdf")


# In[ ]:

url=""


# In[6]:

import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer

http = httplib2.Http()
status, response = http.request('http://dynomapper.com/')

for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
    if link.has_attr('href'):
        print link['href']


# In[14]:

from bs4 import BeautifulSoup
import urllib2

resp = urllib2.urlopen("http://proquest.tech.safaribooksonline.de/book/programming/android/9781785285387")
soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))

for link in soup.find_all('a', href=True):
    with open("x.txt","a") as f:
        f.write(link['href']+"\n")
    #print link['href']


# In[8]:

from time import sleep


# In[9]:

lines = open('x.txt').read().splitlines()


# In[11]:

short="http://proquest.tech.safaribooksonline.de"
for i in range(0,len(lines),2):
    url=short+lines[i]
    pdfu(url)
    print lines[i]
    sleep(10)
    


# In[23]:




# In[ ]:



