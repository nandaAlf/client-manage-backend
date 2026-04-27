from motor.motor_asyncio import AsyncIOMotorClient
from app.utils.config import DATABASE_URL, DATABASE_NAME

client = AsyncIOMotorClient(DATABASE_URL)
db = client[DATABASE_NAME]