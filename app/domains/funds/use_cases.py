"""
Specific use cases for investment funds.
"""
from app.domains.funds.service import FundService

class FundUseCases:
    """Use cases for managing investment funds."""
    
    async def list_funds(self):
        """Use case: List all investment funds."""
        return await FundService().get_funds()
    
    async def get_fund(self, fund_id: str):
        """Use case: Retrieve a specific investment fund."""
        return await FundService().get_fund(fund_id)