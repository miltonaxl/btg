"""API routes for managing investment funds."""

from fastapi import APIRouter, Depends, HTTPException, Request
from app.domains.funds.use_cases import FundUseCases
from app.domains.funds.schemas import FundResponseSchema

router = APIRouter(prefix="/funds", tags=["Funds"])

@router.get("/")
async def list_funds( use_case: FundUseCases = Depends()):
    """Retrieve a list of investment funds."""
    return await use_case.list_funds()