from pymongo import MongoClient
from pymongo.server_api import ServerApi

from src.config import MONGODB_URI

client = MongoClient(
    MONGODB_URI,
    server_api=ServerApi("1")
)

db = client["book_mongodb_chunks"]

collection = db["chunked_data"]