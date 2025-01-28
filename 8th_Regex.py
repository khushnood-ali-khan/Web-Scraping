import requests
from bs4 import BeautifulSoup
import re

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
req = requests.get(url)

soup = BeautifulSoup(req.text,"lxml")
# data = soup.find_all(string="Asus VivoBook...")     #find the exact elements.   
data = soup.find_all(string= re.compile("Lenovo"))    #find everything containing the string.

print(data)