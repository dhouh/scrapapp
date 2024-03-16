# main.py
from fastapi import FastAPI, HTTPException
import requests
import os
from pymongo import MongoClient
app = FastAPI()


# MongoDB connection parameters
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "my_database"
COLLECTION_NAME = "facebook_posts"


def insert_facebook_posts(posts):
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    try:
        result = collection.insert_one(posts)
        print("Posts stored successfully. Inserted IDs:", result)
    except Exception as e:
        print("Error storing posts:", e)

# Facebook page ID and access token
PAGE_ID = "3688049334765083"
ACCESS_TOKEN ="EAAS4GIprWy0BOxc19l9Pyx2pEJmRsOqlorJGFfoFLo9tkZBiio3BDeTWaMPDD2AOoAigEF3tBZB1Fu0XZCgVJYtLugZAHZB08cEPrRRZBlZBtfQzSGT4yt92fsKyv8OGqzVJOiz7nBsyTf6kHBjEWTKSxyDUrikBIZCZCSldjZARirBKJSPP1pzF15YZAxaqYGFcsIc6dFEkVbFQyZCyhxA3wiLaZCBG8M3J9cmUETZCNsclNryfMZB8Saaja2bfsJix9rGlgZDZD"
@app.get("/posts/")
def get_facebook_posts(token=ACCESS_TOKEN):
    url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/posts?fields=message&access_token={token}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        with open("Scrap.json", 'w') as f:  
            for key, value in data.items():  
                f.write('%s:%s\n' % (key, value))
        posts = [post for post in data.get("data", [])]
        insert_facebook_posts(data)
        return {"posts": posts}
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from Facebook")


# Default endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Facebook scraping service."}
