"""
Business logic for financial transactions.
"""
from app.domains.transactions.repository import TransactionRepository
from app.domains.transactions.schemas import TransactionCreateSchema, TransactionResponseSchema
from app.domains.funds.use_cases import FundUseCases
from app.domains.balances.use_cases import BalanceUseCases
from app.domains.users.use_cases import UserUseCases
from fastapi import HTTPException
from app.utils.index import clean_and_format_string, format_number
from app.adapters.email_service import EmailService

class TransactionService:
    """Handles business logic for financial transactions."""
    
    async def get_all_by_user_ip(self, user_id: str):
        """Retrieve all transactions."""
        return await TransactionRepository.get_all_by_user_id(user_id=user_id)

    async def create_transaction(self, transaction_data: TransactionCreateSchema):
        """Create a new financial transaction."""

        fund_id = transaction_data.fund_id
        fund = await FundUseCases().get_fund(fund_id=fund_id)
        
        amount = transaction_data.amount
        fund_amount = fund.minimum_amount
        if amount < fund_amount:
            raise HTTPException(status_code=400, detail=f"El monto mínimo para vincularse al fondo { clean_and_format_string(fund.name ) } es de { format_number(fund_amount) }")
        
        balance_data = await BalanceUseCases().get_balance(user_id=transaction_data.user_id)
        balance = balance_data.balance
        if fund_amount > balance:
            raise HTTPException(status_code=400, detail=f"No tiene saldo disponible para vincularse al fondo {  clean_and_format_string(fund.name ) }")
        
        
        
        new_balance = balance - amount
        
        await BalanceUseCases().update_balance(user_id=transaction_data.user_id, amount=new_balance)
        transaction_data.status = "active"
        await TransactionRepository.create(transaction_data)
        
        user = await UserUseCases().get_by_id(user_id=transaction_data.user_id)
        email = user.email
        print("EMAIL => ", email)
        data_emailed = {"amount": format_number(amount), "fund_name": clean_and_format_string(fund.name) }
        await EmailService().transaction_creation_email(to=email, data=data_emailed)
        return await self.get_all_by_user_ip(user_id=transaction_data.user_id)