"""API routes for managing balances."""
from fastapi import APIRouter, Depends, HTTPException, Request
from app.domains.balances.use_cases import BalanceUseCases

router = APIRouter(prefix="/balances", tags=["Balances"])

@router.get("/")
async def get_balance(request: Request, use_case: BalanceUseCases = Depends()):
    """Retrieve the current balance of a user."""
    user = request.state.user
    balance = await use_case.get_balance(user.id)

    
    return {"balance": balance}