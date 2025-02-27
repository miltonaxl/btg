"""
Specific use cases for financial transactions.
"""
from app.domains.transactions.service import TransactionService
from app.domains.transactions.schemas import TransactionCreateSchema


class TransactionUseCases:
    """Use cases for managing financial transactions."""
    
    async def get_all_by_user_ip(self, user_id: str):
        """Use case: List all transactions."""
        return await TransactionService().get_all_by_user_ip(user_id)

    async def create_transaction(self, data: dict):
        """Use case: Create a financial transaction."""
        
        return await TransactionService().create_transaction(TransactionCreateSchema(**data ))
    