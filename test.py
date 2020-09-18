from utils.data import getJSON
import pymongo
from pymongo import MongoClient

config = getJSON("config.json")

cluster = MongoClient(config.mongoclient)
db = cluster["coins"]
collection = db["coins"]
print(db)
post = {
    "_id": "testid",
    "coins": 0,
    "cookie": 0,
    "apple": 0,
    "choc": 0,
    "poop": 0,
    "afk": "No Status Set",
}
collection.insert_one(post)
print("completed")