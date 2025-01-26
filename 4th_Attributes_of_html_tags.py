import requests
from bs4 import BeautifulSoup

url = "https://www.quora.com/"
req = requests.get(url)

soup = BeautifulSoup(req.text, "lxml")
tag = soup.div
print(tag.attrs)        #Print the attribute of the tag.