from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

def get_database_client():
    uri = os.getenv("MONGODB_URI")

    if not uri:
        raise ValueError("MONGODB_URI not found.")

    client = MongoClient(uri, server_api=ServerApi("1"))
    client.admin.command("ping")
    return client