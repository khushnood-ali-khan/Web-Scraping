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

# print(headers)
df = pd.DataFrame(columns=headers)      #extract only the headers of the column data.
# print(df)
df.to_csv("11th_Extract_table_part1.csv")