""" Base Model for all models in the application """

from datetime import datetime, timezone
from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class BaseModel(BaseModel):
    """Base model for all models in the application."""
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        """Pydantic configuration."""
        json_encoders = {ObjectId: str}
        orm_mode = True

    def __init__(self, **data):
        """Initialize the model."""
        super().__init__(**data)
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)
        
        
class BaseSchemaCreation(BaseModel):
    """Base schema for all response schemas."""
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Config:
        """Pydantic configuration."""
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class BaseSchema(BaseSchemaCreation):
    """Base schema for all response schemas."""
    id: str

    class Config:
        """Pydantic configuration."""
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        
        
        

