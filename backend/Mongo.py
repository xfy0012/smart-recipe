import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

# Load environment variables from .env file
MONGO_URI = os.getenv("MONGODB_URL")

# Create a new client and connect to the server
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

# test connection
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("MongoDB connection successful")
except Exception as e:
    print("MongoDB connection failed", e)

db = client['smartrecipe']  # Replace 'mydatabase' with your database name