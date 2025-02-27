"""
CRUD operations for investment funds in MongoDB.
"""
from app.core.database import database
from app.domains.funds.models import FundModel
from bson import ObjectId

class FundRepository:
    """Handles CRUD operations for investment funds."""
    
    @staticmethod
    async def get_all():
        """Retrieve all investment funds."""
        funds = await database["funds"].find().to_list(100)
        return [FundModel(**{**f, "id": str(f["_id"])}) for f in funds]
    
    @staticmethod
    async def get(fund_id: str):
        """Retrieve a specific investment fund."""
        try:
            print(f"🔍 Searching for fund with ID: {fund_id}")

            # Convert fund_id to ObjectId if needed
            fund = await database["funds"].find_one({"_id": ObjectId(fund_id)})

            print(f"✅ Fund found: {fund}")

            if not fund:
                raise ValueError(f"Fund with ID {fund_id} not found")

            return FundModel(**fund)
        
        except Exception as e:
            print(f"❌ Error fetching fund: {e}")
            raise
