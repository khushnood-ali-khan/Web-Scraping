import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.timeanddate.com/weather/"
req = requests.get(url)
soup = BeautifulSoup(req.text,"lxml")
table = soup.find("table", class_ = "zebra fw tb-theme")
body = table.find_all("tr")


report_list = []
for report in body:
    location = report.find_all("td")
    total_report = [data.text.strip() for data in location if data.text.strip()]
    if len(total_report) > 3:
        total_report.insert(3, "") 
    if len(total_report) > 6:
        total_report.insert(6 ,"") 

    report_list.append(total_report)

df = pd.DataFrame(report_list)
df.to_csv("Weather Report.csv")
# print(report_list)