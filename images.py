import requests as rq
from bs4 import BeautifulSoup as bs
from PIL import Image
from io import BytesIO
import os, sys

def StartSearch():
    search = input("Search for:")
    params = {"q": search}
    r = rq.get("http://www.bing.com/images/search", params)
    dir_name = search.replace(" ","_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    soup = bs(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})


    for item in links:
        try:
            img_obj = rq.get(item.attrs["href"])
            print("Getting", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save("./" + dir_name+ "/" + title, img.format)
            except:
                print("Could not save image")
        except:
            print("Could not request image")

    StartSearch()

StartSearch()