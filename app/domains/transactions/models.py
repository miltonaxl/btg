"""
Database model for financial transactions.
"""
from app.core.bases_database import BaseModel

from bson import ObjectId
from app.utils.index import PyObjectId



class TransactionModel(BaseModel):
    """Transaction model."""
    user_id: PyObjectId
    fund_id: PyObjectId
    status: str = "active"
    amount: float

    class Config:
        orm_mode = True
        json_encoders = {ObjectId: str}
