import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.timeanddate.com/weather/"
req = requests.get(url)
soup = BeautifulSoup(req.text,"lxml")
table = soup.find("table", class_ = "zebra fw tb-theme")
body = table.find("tbody")

report_list = []

for report in body.find_all("tr"):
    # time = report.find("")
    report_list.append(report.text)

print(report_list)