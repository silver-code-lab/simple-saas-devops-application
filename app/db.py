import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
DB_NAME = os.getenv("DB_NAME", "peopledb")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
people_coll = db["people"]
