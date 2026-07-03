from src.database import get_database_client

try:
    client = get_database_client()
    print("✅ MongoDB Atlas connected successfully!")
except Exception as e:
    print(e)