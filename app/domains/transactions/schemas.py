"""
Pydantic schemas for transaction validation.
"""
from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from bson import ObjectId
from app.core.bases_database import BaseSchema, BaseSchemaCreation

class TransactionCreateSchema(BaseSchemaCreation):
    """Schema for creating a financial transaction."""
    user_id: Optional[str] = None
    fund_id: str
    amount: float
    status: Optional[str] = "active"
    

class TransactionResponseSchema(BaseSchema):
    """Schema for returning transaction data."""
    id: str
    fund: dict
    amount: float
    status: str
    created_at: datetime
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
    