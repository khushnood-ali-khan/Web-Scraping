import requests
from bs4 import BeautifulSoup

url = "https://www.quora.com/"
req = requests.get(url)             #send a requests to the website.

soup = BeautifulSoup(req.text,"lxml")       #requests for the html code using BeautifulSoup library.
print(soup)