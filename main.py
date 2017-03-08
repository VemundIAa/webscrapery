from bs4 import BeautifulSoup as bs
import requests as rq


search = input("Enter search term:")
params = {"q": search}
r = rq.get("http://www.bing.com/search", params)

soup = bs(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item.text and item_href:
        print(item_text)
        print(item_href)
        print("Summary:", item.find("p").text)
