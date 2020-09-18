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
    "bank": 0,
    "maxbank": 100,
    "purse": 0,
}
collection.insert_one(post)
print("completed")