"""
Application configuration module.
This module defines the settings for the FastAPI application,
including project metadata and database connection details.
"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application configuration using Pydantic to manage environment variables."""
    PROJECT_NAME: str = "FastAPI Hexagonal API"
    PROJECT_VERSION: str = "1.0.0"
    MONGO_URI: str = "mongodb://localhost:27017"
    MONGO_DB: str = "fastapi_db"
    
    # MAILJET API KEYS VARIUABLES 
    MAILJET_API_KEY: str=" MAILJET_API_KEY"
    MAILJET_SECRET_KEY: str=" MAILJET_SECRET_KEY"
    MAILJET_EMAIL: str= "MAILJET_EMAIL"
    MAILJET_TEMPLATE_TRANSACTION: str="MAILJET_TEMPLATE_TRANSACTION"
    
    class Config:
        """Additional configuration to load variables from a .env file."""
        env_file = ".env"

settings = Settings()
