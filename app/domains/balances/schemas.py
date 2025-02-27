"""Pydantic schemas for balance validation."""
from pydantic import BaseModel

class BalanceResponseSchema(BaseModel):
    """Schema for returning user balance."""
    balance: float
    
    
class BalanceCreateSchema(BaseModel):
    """Schema for creating a user balance."""
    user_ip: str
    balance: float