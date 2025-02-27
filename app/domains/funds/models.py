"""
Database model for investment funds.
"""

from typing import Optional
from bson import ObjectId
from app.core.bases_database import BaseModel

class FundModel(BaseModel):
    """Investment fund model."""
    name: str 
    category: str
    minimum_amount: float

    class Config:
        orm_mode = True
        json_encoders = {ObjectId: str}
        