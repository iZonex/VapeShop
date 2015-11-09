from settings import *
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(DB_URL)
db = client[DB_NAME]
