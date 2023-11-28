import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://udn.com/news/breaknews/1"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the headline elements
headlines = soup.find_all("div", class_="story-list__text")

# Extract the text and URL from each headline element and print
for headline in headlines:
    headline_text = headline.text.strip()
    headline_url = urljoin(url, headline.a["href"])
    print(headline_text)
    print(headline_url)
