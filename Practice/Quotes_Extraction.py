import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
req = requests.get(url)

soup = BeautifulSoup(req.text, "lxml")
body = soup.find_all("div", class_ = "quote")
lines_list, author_list,tag_list = [],[],[]
# quotes = soup.find_all("div", class_ = "quote")
for quote in body:
    lines = quote.find("span", class_ = "text").text
    authors = quote.find("small", class_ = "author").text
    tags = [tag.text for tag in quote.find_all("a", class_ = "tag")]

    lines_list.append(lines)
    author_list.append(authors)
    tag_list.append(tags)

df = pd.DataFrame({
    "Lines":lines_list,
    "Author Name":author_list,
    "Tags":tag_list
})
# print(df)
df.to_csv("Quotes.csv")