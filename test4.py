import requests, time
from bs4 import BeautifulSoup

url = "https://www.nkust.edu.tw/p/403-1000-1363-1.php?Lang=zh-tw"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("div", class_="news_title")

for headline in headlines:
    headline_url = headline.find("a")["href"]
    content_response = requests.get(headline_url)
    content_soup = BeautifulSoup(content_response.text, "html.parser")
    content = content_soup.find("div", class_="content")
    print(content.text.strip())
    time.sleep(3)
