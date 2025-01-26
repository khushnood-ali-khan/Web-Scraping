import requests
from bs4 import BeautifulSoup

url = "https://www.quora.com/"
req = requests.get(url)

soup = BeautifulSoup(req.text,"lxml")
print(soup.div)                     #include the specific tag that data you want like (div, p, h1, h2 etc).