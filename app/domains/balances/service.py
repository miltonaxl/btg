"""Business logic for user balances."""
from app.domains.balances.repository import BalanceRepository
from app.domains.balances.schemas import BalanceResponseSchema
from fastapi import HTTPException

class BalanceService:
    """Handles business logic for user balances."""

    async def get_balance(self, user_id: str):
        """Retrieve the current balance of a user."""
        balance_doc = await BalanceRepository.get_balance(user_id)
        return BalanceResponseSchema(balance=balance_doc.get("balance"))

    async def update_balance(self, user_id: str, amount: float):
        """Update user balance and return success status."""
        
        
        if amount < 0:
            raise HTTPException(status_code=400, detail="Invalid amount.")

        await BalanceRepository.update_balance(user_id, amount)
        
        return BalanceResponseSchema(user_id=user_id, balance=amount)
        
    
    async def create_balance(self, user_id: str):
        """Create a new balance for a user."""
        return await BalanceRepository.create_balance(user_id)