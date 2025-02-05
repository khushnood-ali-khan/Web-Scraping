import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Web_scraping"
req = requests.get(url)

soup = BeautifulSoup(req.text,"lxml")
body = soup.find("div", class_ = "mw-content-ltr mw-parser-output")
print(body.text)