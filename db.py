from pymongo import MongoClient

# 🔴 Replace with your MongoDB Atlas connection string
MONGO_URI = "YOUR_MONGO_URI"

client = MongoClient(MONGO_URI)
db = client["appointment_db"]

users_collection = db["users"]
appointments_collection = db["appointments"]
