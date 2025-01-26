import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
req = requests.get(url)

soup = BeautifulSoup(req.text, "lxml")
# find = soup.find('div')                 #find the first div in the html and print it.

# print(find)

dec1 = soup.find("p", {"class":"description card-text"})
dec = soup.find("p", class_ = "description card-text")

print(dec.string, dec1)