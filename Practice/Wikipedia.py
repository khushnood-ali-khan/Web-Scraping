import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/Web_scraping"
req = requests.get(url)

soup = BeautifulSoup(req.text,"lxml")
paragraphs = soup.find_all("p")

paragraph_list = []

for text in paragraphs :
    paragraph_list.append(text.text)

print(paragraph_list)