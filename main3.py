from fastapi import FastAPI, Request
from facebook_scraper import get_posts
import datetime

import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

app = FastAPI()
client = MongoClient("localhost", 27017)
db = client["scrapedPosts"]
collection = db["posts"]

app = FastAPI()

def scrap_facebook_page(page_name):
    for post in get_posts(page_name,pages=None,timeout=None,extra_info=True,options={"comments": True,"reactors": True}):
        print(post)

page_name='Machine.Learning.Artificial.Intelligence'


@app.get("/")
async def root():
    return "Welcome to my facebook scraping service"

@app.get("/scrap/{page_name}")
def scrap(page_name,save: bool=True):
    res={}
    posts_list=[]
    item= {
        'page name': page_name,
        'post': 'post test',
        'reacts': 63
    }
    posts_list.append(item)

    res["result"] = posts_list
    res["time"] = datetime.datetime.now()
    if save:
        try: 
            collection.insert_many(posts_list)
            return "saved successfully"
        except:
            return "saving error"
    return posts_list
