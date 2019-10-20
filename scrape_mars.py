#!/usr/bin/env python
# coding: utf-8
import os
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import time
import pandas as pd
# import pymongo


# In[2]:
def scrape():

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    mars_data = {}

# In[3]:


    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(5)

# In[4]:
    html = browser.html
    soup = bs(html, 'html.parser')
    time.sleep(5)

# In[5]:
    mars_data["news_title"] = soup.find('div', class_='content_title').get_text()

# In[6]:
    mars_data["news_p"] = soup.find('div', class_='article_teaser_body').get_text()
# In[7]:
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(5)
# In[8]:

    html = browser.html
    soup_pic = bs(html, 'html.parser')
    time.sleep(5)
# In[9]:
    img = browser.find_link_by_partial_text('FULL')
    img.click()
    time.sleep(4)
# In[10]:

    img = browser.find_link_by_partial_text('more info')
    img.click()
    time.sleep(5)

# In[11]:

    html = browser.html
    soup_pic = bs(html, 'html.parser')
# In[12]:
    results = soup_pic.find('img', class_="main_image")['src']

# In[13]:
    featured_img_url = "https://www.jpl.nasa.gov" + results
    time.sleep(5)
    mars_data["featured_img_url"] =  "https://www.jpl.nasa.gov" + results
# In[14]:
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    time.sleep(5)
# In[15]:

    html = browser.html
    soup = bs(html, 'html.parser')
    time.sleep(5)

# In[16]:
    mars_data["mars_weather"]= soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').get_text()
# In[17]:
    facts_url = "https://space-facts.com/mars/"
    tables = pd.read_html(facts_url)
    time.sleep(5)
# In[19]:
    df = tables[1]
    time.sleep(5)
    df.columns = ['Description', 'Value']
# In[20]:
    mars_data["html_table"] = df.to_html(index=False)
    time.sleep(5)


# In[22]:
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(5)


# In[23]:


    html = browser.html
    soup = bs(html, 'html.parser')
    time.sleep(5)


# In[24]:


    img = browser.find_link_by_partial_text('Cerberus')
    img.click()
    time.sleep(4)


# In[25]:


    img = browser.find_link_by_partial_text('Open')
    img.click()
    time.sleep(4)


# In[26]:


    html_hemi_pic1 = browser.html
    soup_hemi1= bs(html_hemi_pic1, 'html.parser')


# In[27]:


    hemi1 = soup_hemi1.find('img', class_="wide-image")['src']

# In[28]:


    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(4)


# In[29]:


    img = browser.find_link_by_partial_text('Schiaparelli')
    img.click()
    time.sleep(4)


# In[30]:


    img = browser.find_link_by_partial_text('Open')
    img.click()
    time.sleep(4)


# In[31]:


    html_hemi_pic2 = browser.html
    soup_hemi2= bs(html_hemi_pic2, 'html.parser')
# In[32]:

    hemi2 = soup_hemi2.find('img', class_="wide-image")['src']


# In[33]:


    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(5)


# In[34]:


    img = browser.find_link_by_partial_text('Syrtis Major')
    img.click()
    time.sleep(4)


# In[35]:


    img = browser.find_link_by_partial_text('Open')
    img.click()
    time.sleep(4)


# In[36]:


    html_hemi_pic3 = browser.html
    soup_hemi3= bs(html_hemi_pic3, 'html.parser')


# In[37]:
    hemi3 = soup_hemi3.find('img', class_="wide-image")['src']



# In[38]:


    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(5)


# In[39]:


    img = browser.find_link_by_partial_text('Valles Marineris')
    img.click()
    time.sleep(4)


# In[40]:


    img = browser.find_link_by_partial_text('Open')
    img.click()
    time.sleep(4)


# In[41]:


    html_hemi_pic4 = browser.html
    soup_hemi4= bs(html_hemi_pic4, 'html.parser')


# In[42]:


    hemi4 = soup_hemi4.find('img', class_="wide-image")['src']


# In[43]:


    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov" + hemi1},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov" + hemi2},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov" + hemi3},
        {"title": "'Valles Marineris", "img_url": "https://astrogeology.usgs.gov" + hemi4},
    ]


    mars_data["hemispheres"] = hemisphere_image_urls

    browser.quit()
    return mars_data

