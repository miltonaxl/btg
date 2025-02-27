""" Routers for the API. """
from fastapi import APIRouter, Depends
from app.api.routers import transactions, balances, funds, users
from app.middlewares.validate_resource import validate_request

api_router = APIRouter()
api_router.include_router(transactions.router, dependencies=[Depends(validate_request)])
api_router.include_router(balances.router, dependencies=[Depends(validate_request)])
api_router.include_router(funds.router)
api_router.include_router(users.router)



