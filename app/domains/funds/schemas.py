"""
Pydantic schemas for investment funds validation.
"""
from pydantic import BaseModel


class FundResponseSchema(BaseModel):
    """Schema for returning investment fund data."""
    id: str
    name: str
    category: str
    minimum_amount: float