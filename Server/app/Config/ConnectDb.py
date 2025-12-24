from motor.motor_asyncio import AsyncIOMotorClient
from app.Config.Config import setting

url = setting.DB_URL
client = AsyncIOMotorClient(url)

db = client["clearday"]

collection_user = db["users"]
collection_subscription = db["subscriptions"]