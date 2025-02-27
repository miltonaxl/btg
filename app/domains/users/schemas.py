"""
Pydantic schemas for user validation identified by IP.
"""
import re
from pydantic import BaseModel, EmailStr, Field
from app.core.bases_database import BaseSchema,BaseSchemaCreation
from bson import ObjectId
from typing import Optional



class UserCreateSchema(BaseSchemaCreation):
    """Schema for creating a user identified by IP."""
    ip: str = None
    full_name: str
    email: EmailStr
    phone: str = Field(..., pattern=r"^\d{10,11}$")
    
class BalanceSchema(BaseModel):
    """Schema for user balance."""
    balance: float
class UserSchema(BaseSchema):
    """Schema for a user identified by IP."""
    ip: str
    full_name: str
    email: str
    phone: str
    balance: Optional[BalanceSchema] = None
    
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
    