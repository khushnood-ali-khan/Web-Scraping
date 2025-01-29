import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
req = requests.get(url)

soup = BeautifulSoup(req.text,"lxml")
name = soup.find_all("a", {"class" : "title"})
price = soup.find_all("h4", class_ = "price float-end card-title pull-right")
desc = soup.find_all("p", class_ = "description card-text")
review = soup.find_all("p", class_ = "review-count float-end")

name_list, price_list, desc_list, review_list = [],[],[],[]

# length = len(name)
# for i in range(length):
#     names = name[i].text
#     prices = price[i].text
#     description = desc[i].text
#     reviews = review[i].text
#     name_list.append(names)
#     price_list.append(prices)
#     desc_list.append(description)
#     review_list.append(reviews)

for names, prices, description, reviews in zip (name,price,desc, review):
    name_list.append(names.text)
    price_list.append(prices.text)
    desc_list.append(description.text)
    review_list.append(reviews.text)

data = pd.DataFrame({
    "Product Name ":name_list,
    "Descreption":desc_list,
    "Price":price_list,
    "Reviews":review_list
})

# print(data)
# data.to_csv("data.csv")       #Save to csv format file
data.to_csv("data1.csv")