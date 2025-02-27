"""
Database configuration module.
Handles the connection to MongoDB using Motor.
"""
import motor.motor_asyncio
from app.core.config import settings

"""Database client instance for MongoDB connection."""
client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URI)
database = client[settings.MONGO_DB]






