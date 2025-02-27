"""Database model for user balances."""

from bson import ObjectId
from app.core.bases_database import BaseModel
from app.utils.index import PyObjectId

class BalanceModel(BaseModel):
    """Balance model representing user funds."""
    user_id: PyObjectId
    balance: float

    class Config:
        orm_mode = True
        json_encoders = {ObjectId: str}