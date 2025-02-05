import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.bbc.com/news"
req = requests.get(url)
soup = BeautifulSoup(req.text,"lxml")
headlines = soup.find_all("h2")
title = []
for head_lines in headlines:
    title.append(head_lines.text)

df = pd.DataFrame({"To DayHeadlines":title})
df.to_csv("headlines.csv")