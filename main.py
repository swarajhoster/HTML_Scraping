import requests
from bs4 import BeautifulSoup

# Website To be Scraped
url = "https://codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')

# Step 3: HTML Tree traversal( GET specific TAG )

# Get title of the PAGE
title = soup.title

# Get all the p tag of the PAGE
paras = soup.find_all('p')

# Get first element of the PAGE and only the class name
o_p = soup.find('p')['class']

# Get All links in the page
anchors = soup.find_all('a')
all_links = set()

# Get all links in the page:
for link in anchors:
    if link.get('href') != "#":
        link_url = url + link.get('href')
        all_links.add(link)
        # print(link_url)

