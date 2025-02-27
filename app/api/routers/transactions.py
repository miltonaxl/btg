"""API routes for managing financial transactions."""
from fastapi import APIRouter, Depends, HTTPException, Request
from app.domains.transactions.use_cases import TransactionUseCases
from app.domains.transactions.schemas import TransactionCreateSchema
from app.core.shared.decorators.validate_schemas import ValidateSchemas

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("/")
async def get_transactions( request: Request, use_case: TransactionUseCases = Depends()):
    """Retrieve a list of financial transactions."""
    user_id = request.state.user.id
    return await use_case.get_all_by_user_ip(user_id=user_id)

@router.post("/subscribe")
async def subscribe_to_fund(
    request: Request,
    _: TransactionCreateSchema = Depends(ValidateSchemas(TransactionCreateSchema)), 
    use_case: TransactionUseCases = Depends()
):
    """Subscribe to an investment fund."""
    data = await request.json()
    return await use_case.create_transaction(data)

@router.delete("/{transaction_id}")
async def cancel_subscription(transaction_id: str, use_case: TransactionUseCases = Depends()):
    """Cancel a fund subscription."""
    success = await use_case.cancel_transaction(transaction_id)
    if not success:
        raise HTTPException(status_code=404, detail="Transaction not found.")
    
    return {"message": "Subscription canceled successfully."}
