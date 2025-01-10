from pymongo import MongoClient
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

database_url = os.getenv("MONGODB_URI")
client = MongoClient(database_url)

db = client.gameRec

games_collection = db["games"]
users_collection = db["users"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)