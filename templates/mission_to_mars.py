#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from datetime import datetime
import os
import time


# In[2]:


executable_path ={'executable_path': 'chromedriver.exe'}
browser = Browser("chrome", **executable_path, headless=False)


# In[3]:


url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[4]:


html = browser.html
news_soup = BeautifulSoup(html, "html.parser")

slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[5]:


slide_elem.find("div", class_='content_title')


# In[6]:


news_title = slide_elem.find("div", class_="content_title").get_text()
news_title
news_p = slide_elem.find("div", class_="article_teaser_body").get_text()
news_p


# In[7]:


url_image= "https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit"
browser.visit(url_image)


# In[8]:


full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[9]:


browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.find_link_by_partial_text('more info')
more_info_elem.click()


# In[10]:


html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')


# In[11]:


img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[12]:


img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# In[13]:


url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)


# In[14]:


html = browser.html
weather_soup = BeautifulSoup(html, 'html.parser')


# In[15]:


mars_weather_tweet = weather_soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})


# In[16]:


mars_weather = mars_weather_tweet.find('p', 'tweet-text').get_text()


# In[17]:


url ='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhance&k1=target&v1=Mars'
browser.visit(url)


# In[18]:


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


# In[19]:


hemisphere_image_urls


# In[20]:


df = pd.read_html('https://space-facts.com/mars/')[1]
#df.columns=['description', 'value']
#df.set_index('description', inplace=True)
df


# In[21]:


df.to_html()


# In[22]:


browser.quit()


# In[ ]:




