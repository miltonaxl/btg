"""Specific use cases for user balances."""
from app.domains.balances.service import BalanceService

class BalanceUseCases:
    """Use cases for managing user balances."""

    async def get_balance(self, user_id: str):
        """Use case: Retrieve user balance."""
        return await BalanceService().get_balance(user_id)

    async def update_balance(self, user_id: str, amount: float):
        """Use case: Update user balance."""
        return await BalanceService().update_balance(user_id, amount)
    
    async def create_balance(self, user_id: str):
        """Use case: Create user balance."""
        return await BalanceService().create_balance(user_id)