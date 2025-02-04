import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/Web_scraping"
req = requests.get(url)

soup = BeautifulSoup(req.text,"lxml")
paragraphs = soup.find_all("p")
heading = soup.find_all("h2")


paragraph_list = []
heading_list = []

for text, title in zip (paragraphs, heading):
    paragraph_list.append(text.text)
    heading_list.append(title.text)

print(paragraph_list,heading_list)