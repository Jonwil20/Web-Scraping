#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import os
import time
from flask import Flask
from selenium import webdriver
import requests


# In[2]:


executable_path ={'executable_path': 'chromedriver.exe'}
browser = Browser("chrome", **executable_path, headless=False)


# In[3]:


url = "https://mars.nasa.gov/news/"
response = requests.get(url)


# In[4]:


html = browser.html
news_soup = BeautifulSoup(response.text, "html.parser")


# In[5]:


news_title = news_soup.find("div", class_="content_title").text.strip()
news_title


# In[6]:


news_para = news_soup.find('div', class_='rollover_description_inner').text.strip()
news_para


# In[7]:


url_image= "https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit"


# In[8]:


full_image_elem = browser.find_by_id('full_image')


# In[9]:


html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')
image_url = img_soup.find('img', class_='fancybox-image')


# In[10]:


img_url_rel = "https://www.jpl.nasa.gov"
img_url_rel


# In[11]:


url_1 = 'https://twitter.com/marswxreport?lang=en'
response1 = requests.get(url_1)


# In[12]:


weather_soup = BeautifulSoup(response.text, 'html.parser')


# In[13]:


mars_weather_tweet = weather_soup.find('div', class_= 'js-tweet-text-container')


# In[14]:


url_2 ='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhance&k1=target&v1=Mars'
response2 = requests.get(url_2)


# In[15]:


hemisphere_image_urls = []

links = browser.find_by_css("a.product-item h3")

for i in range(len(links)):
    hemisphere = {}
    
    browser.find_by_css("a.product-item h3")[i].click()
    
    sample_elem = browser.find_link_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']
    
    hemisphere['title'] = browser.find_by_css("h2.title").text
    
    hemisphere_image_urls.append(hemisphere)
    
    browser.back()


# In[16]:


hemisphere_image_urls


# In[17]:


df = pd.read_html('https://space-facts.com/mars/')[1]
#df.columns=['description', 'value']
#df.set_index('description', inplace=True)
df


# In[18]:


df.to_html()


# In[19]:


url_hemi1 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
response = requests.get(url_hemi1)


# In[20]:


soup_hemi1 = BeautifulSoup(response.text, 'html.parser')


# In[21]:


hemi1_title = soup_hemi1.find('h2', class_='title')


# In[22]:


url_hemi2 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
response = requests.get(url_hemi2)


# In[23]:


soup_hemi2 = BeautifulSoup(response.text, 'html.parser')


# In[24]:


hemi2_title = soup_hemi2.find('h2', class_='title')


# In[25]:


url_hemi3 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
response = requests.get(url_hemi3)


# In[26]:


soup_hemi3 = BeautifulSoup(response.text, 'html.parser')


# In[27]:


hemi3_title = soup_hemi3.find('h2', class_='title')


# In[28]:


url_hemi4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
response = requests.get(url_hemi4)


# In[29]:


soup_hemi4 = BeautifulSoup(response.text, 'html.parser')


# In[30]:


hemi4_title = soup_hemi4.find('h2', class_='title')


# In[31]:


browser.quit()


# In[ ]:




