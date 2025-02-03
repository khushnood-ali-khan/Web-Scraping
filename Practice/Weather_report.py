import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.timeanddate.com/weather/"
req = requests.get(url)
soup = BeautifulSoup(req.text,"lxml")
table = soup.find("table", class_ = "zebra fw tb-theme")
body = table.find_all("tr")


report_list = []
report = 1
for report in body:
    location = report.find_all("td")
    report_list.append([data.text.strip() for data in location])

print(report_list)