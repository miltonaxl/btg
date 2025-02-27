"""
Dependency injection module.
Provides shared dependencies for the FastAPI application.
"""
from fastapi import Depends
from app.core.database import database

def get_database():
    """Dependency to get the database instance."""
    return database