import requests, json
res = requests.get("https://ecshweb.pchome.com.tw/search/v4.3/all/results?q=iphone%2013&page=2&sort=rnk/dc", {
  "headers": {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "x-requested-with": "XMLHttpRequest"
  },
  "referrer": "https://ecshweb.pchome.com.tw/search/v3.3/?q=iphone%2013",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": None,
  "method": "GET",
  "mode": "cors",
  "credentials": "omit"
}).text
data = json.loads(res)
products = data["Prods"]
for p in products:
    print(p['Name'], ":", p['Price'], "元")