import requests
import json

url = "https://ecshweb.pchome.com.tw/search/v3.3/?q=iphone%2013"

response = requests.get(url)
data = response.json()

products = data["prods"]

for product in products:
    print(product["name"])
