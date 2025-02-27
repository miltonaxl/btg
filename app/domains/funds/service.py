"""
Business logic for investment funds.
"""
from app.domains.funds.repository import FundRepository
from app.domains.funds.schemas import  FundResponseSchema
from fastapi import HTTPException

class FundService:
    """Handles business logic for investment funds."""
    
    async def get_funds(self):
        """Retrieve all investment funds."""
        return await FundRepository.get_all()

    async def get_fund(self, fund_id: str):
        """Retrieve a specific investment fund."""
        
        get_fund = await FundRepository.get(fund_id)
        if not get_fund:
            raise HTTPException(status_code=404, detail="Fund not found.")
        
        return get_fund