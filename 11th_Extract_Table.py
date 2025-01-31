import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://ticker.finology.in/"
req = requests.get(url)
# print(req)

soup = BeautifulSoup(req.text,"lxml")
table = soup.find("table", class_ = "table table-sm table-hover screenertable")
header = table.find_all("th")

headers = []
for title in header:
    headers.append(title.text)

row = table.find_all("tr")
row_list = []
for rows in row:
    data = rows.find_all("td")
    row_list.append([dat.text.strip() for dat in data])

df = pd.DataFrame(row_list,columns=headers)
df.to_csv("11th_Extract_table.csv")