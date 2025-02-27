from app.core.database import database
from app.domains.transactions.models import TransactionModel
from app.utils.index import normalize_and_convert_ids
from bson import ObjectId
from .schemas import TransactionResponseSchema

class TransactionRepository:
    """Handles CRUD operations for transactions."""
    
    @staticmethod
    async def get_all_by_user_id(user_id: str):
        """Retrieve transactions by user ID, including fund data."""
        pipeline = [
            {
                "$match": {
                    "user_id": user_id
                }
            },
            {
                "$addFields": {
                    "fund_id": {"$toObjectId": "$fund_id"}
                }
            },
            {
                "$lookup": {
                    "from": "funds",
                    "localField": "fund_id",
                    "foreignField": "_id",
                    "as": "fund"
                }
            },
            {
                "$unwind": {
                    "path": "$fund",
                    "preserveNullAndEmptyArrays": True
                }
            }
        ]

        transactions = await database["transactions"].aggregate(pipeline).to_list(None)
        transactions = normalize_and_convert_ids(transactions)
        
        return [TransactionResponseSchema(**t) for t in transactions]

    @staticmethod
    async def create(transaction: TransactionModel):
        """Create a new transaction."""
        result = await database["transactions"].insert_one(transaction.model_dump())
        return str(result.inserted_id)
    
    
    @staticmethod
    async def get_by_id(transaction_id: str):
        """Retrieve a specific transaction by ID."""
        transaction = await database["transactions"].find_one({"_id": transaction_id})
        return TransactionModel(**transaction)
