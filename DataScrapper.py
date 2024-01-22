#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install beautifulsoup4 requests pandas


# In[7]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website you want to scrape
url = "http://quotes.toscrape.com/page/1/"

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text,'html.parser')

    # Extract data from the website using BeautifulSoup
    # Replace the following with the appropriate CSS selectors or other methods
    data_elements = soup.select(".author, .tags , .text")

    # Extract data and store it in a list
    data = [element.text.strip() for element in data_elements]

    # Create a Pandas DataFrame
    df = pd.DataFrame({"Data": data})

    # Save the DataFrame to a CSV file
    df.to_csv("output.csv", index=False)
    print("Data downloaded successfully.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


# In[3]:


import os
current_directory=os.getcwd()
current_directory


# In[ ]:




