
# coding: utf-8

# In[1]:


#Python Web scraping- National Weather Service- San Fransico Bay Area

#Import the request library for webscraping
import requests


# In[2]:


#The request function will request the website to download the content, response is the 
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.3387&lon=-121.8854#.XDE9jS2ZNQI")
page


# In[3]:


#After running the request, we get a Response object. A status_code of 200 means that the page downloaded successfully. We won't fully dive into status codes here, 
#A code 2 generally indicates success, and a code starting with a 4 or a 5 indicates an error.

page.status_code


# In[20]:


#We can print out the HTML content of the page using the content property:

page.content


# In[18]:


#Parsing a page with BeautifulSoup library from Python and create an instance of the BeautifulSoup class. 
from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, 'html.parser')


# In[19]:


#Now print out the HTML content of the page, formatted nicely, using prettify on the BeautifulSoup object:
print(soup.prettify())


# In[12]:


#We want to extract the seven day forecast from the website and find the seven day forecast using find function.
seven_day = soup.find(id ="seven-day-forecast")
#Search the forecast item of the class
forecast_items = seven_day.find_all(class_ ="tombstone-container")

tonight = forecast_items[0]

print(tonight.prettify())


# In[13]:


# extract the data from the page
period = tonight.find(class_="period-name").get_text()
desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp temp-high").get_text()
print(period)
print(desc)
print(temp)


# In[14]:


# extract title

img = tonight.find("img")
t_desc = img['title']
print(t_desc)


# In[15]:


#Extracting all information from the page

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text()for pt in period_tags]
periods


# In[16]:


short_desc = [sd.get_text()for sd in seven_day.select(".tombstone-container .short-desc")]
temp = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
desc = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(short_desc)
print(temp)
print(desc)


# In[17]:


# put as dataframe

import pandas as pd
weather = pd.DataFrame({"Period":periods, "Short_desc":short_desc, "Temperatures": temp, "Description": desc})
weather

