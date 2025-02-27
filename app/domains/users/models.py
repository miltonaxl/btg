"""
Database model for users identified by IP address.
"""
from app.core.bases_database import BaseModel
from typing import Optional
from bson import ObjectId

class UserModel(BaseModel):
    """User model based on IP."""
    ip: str
    full_name: str
    email: str
    phone: str

    class Config:
        orm_mode = True
        json_encoders = {ObjectId: str}