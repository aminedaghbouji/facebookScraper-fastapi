from fastapi import FastAPI
from facebook_scraper import get_posts

from pymongo import MongoClient
from bson.objectid import ObjectId

app = FastAPI()
client = MongoClient("localhost", 27017)
db = client["scrapedPosts"]
collection = db["posts"]

app = FastAPI()


@app.get("/")
async def root():
    return "Welcome to my facebook scraping service"

@app.get("/scrap/{page_name}")
def scrap(page_name,save: bool=True):
    result = {}
    result["scrapedPosts"] = [post for post in get_posts(page_name, pages=None)]
    if save:
        try: 
            collection.insert_many(result["scrapedPosts"])
            return "Scraped posts saved successfully in Database. Please check your Mongo Database to view your data."
        except:
            return "Saving error"
    return result["scrapedPosts"]
