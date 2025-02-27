"""CRUD operations for user balances in MongoDB."""
from app.core.database import database
from bson import ObjectId

INITIAL_BALANCE = 500000

class BalanceRepository:
    """Handles CRUD operations for balances."""

    @staticmethod
    async def get_balance(user_id: str):
        """Retrieve user balance. If not found, initialize it."""
        balance_doc = await database["balances"].find_one({"user_id": ObjectId(user_id)})
        if balance_doc is None:
            return None
        return balance_doc

    @staticmethod
    async def update_balance(user_id: str, new_balance: float):
        """Update user balance based on transaction type."""
        return await database["balances"].update_one({"user_id": user_id}, {"$set": {"balance": new_balance}})
    
    @staticmethod
    async def create_balance(user_id: str):
        """Create a new balance for a user."""
        await database["balances"].insert_one({"user_id": user_id, "balance": INITIAL_BALANCE})
        return INITIAL_BALANCE