#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[3]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[ ]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
print(slide_elem)


# In[ ]:


for i in news_soup.find_all('div', class_="list_text"):
    print(i)
slide_elem = news_soup.select_one('div.list_text')
print("--------------------------------------------")
print(slide_elem)


# In[ ]:


slide_elem.find('div', class_='content_title')


# In[ ]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[ ]:


# Use the parent element to find the first `a` tag and save it as `article_summary`
article_summary = slide_elem.find('div', class_='article_teaser_body').get_text()
article_summary


# In[ ]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images
# 

# In[ ]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[ ]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[ ]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[ ]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[ ]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Tables

# In[ ]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[ ]:


df.to_html()


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# Hemispheres

# In[4]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[5]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
hemisphere_image_urls_titles_soup = soup(html, 'html.parser')

for image_titles in hemisphere_image_urls_titles_soup.find_all('div', class_='item'):
    # Create dictionary
    dict1 = {}
    
    # Get name of image and add it to dictionary
    dict1['name'] = image_titles.find('img', class_='thumb').get('alt').replace(" thumbnail", "")
    image_url_name =image_titles.find('img', class_='thumb').get('alt').lower()
    # hemisphere_image_urls.append(dict1)
    
    url = 'https://marshemispheres.com/' + image_url_name.split()[0] + '.html'
    browser.visit(url)
    html = browser.html
    hemisphere_image_links = soup(html, 'html.parser')
       
    hemisphere_image_link = hemisphere_image_links.select_one('li').a.get('href')
    
    dict1['img_url'] = "https://marshemispheres.com/" + hemisphere_image_link
    hemisphere_image_urls.append(dict1)
    browser.back()


# In[6]:


# 4. Print the list that holds the dictionary of each image url and title.
print(hemisphere_image_urls)


# In[7]:


# 5. Quit the browser
browser.quit()

