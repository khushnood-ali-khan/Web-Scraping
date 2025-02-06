import requests
from bs4 import BeautifulSoup

url = "https://www.daraz.pk/catalog/?spm=a2a0e.tm80335142.search.d_go&q=teady%20bear"
req = requests.get(url)
# print(req)
soup = BeautifulSoup(req.text, "lxml")