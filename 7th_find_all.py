import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
req = requests.get(url)

soup = BeautifulSoup(req.text,"lxml")
name = soup.find_all("a", {"class" : "title"})
price = soup.find_all("h4", class_ = "price float-end card-title pull-right")
desc = soup.find_all("p", class_ = "description card-text")

l = len(name)
# print(len(price))
for i in range (l):
    print(i,": ",name[i].string,": ",price[i].string,": ",desc[i].string)