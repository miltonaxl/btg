from app.core.database import database
from bson import ObjectId
from app.domains.users.schemas import UserCreateSchema
from app.utils.index import normalize_and_convert_ids
from app.domains.users.schemas import UserSchema

class UserRepository:
    """Handles CRUD operations for users identified by IP."""
    
    
    async def __get_by_filter(self, filter_criteria: dict):
        """Retrieve a user by a specific filter."""
        
        
        pipeline_grouped_balance = [
            
            {
                "$match": filter_criteria
            },
            {
                "$lookup": {
                    "from": "balances",
                    "localField": "_id",
                    "foreignField": "user_id",
                    "as": "balance"
                }
            },
            {
                "$unwind": {
                    "path": "$balance",
                    "preserveNullAndEmptyArrays": True
                }
            }
        ]
        
        
        user = normalize_and_convert_ids(await database["users"].aggregate(pipeline_grouped_balance).to_list(None))
        
        return UserSchema(**user[0]) if user else None
    
    
    async def get_by_ip(self, user_ip: str):
        """Retrieve a user by IP."""
        return  await self.__get_by_filter({"ip": user_ip})
    
    
    async def get_by_email(self, email: str):
        """Retrieve a user by email."""
        return await self.__get_by_filter({"email": email})
    
    async def get_by_id(self, user_id: str):
        """Retrieve a user by ID."""
        return await self.__get_by_filter({"_id": ObjectId(user_id)})

    @staticmethod
    async def register_user(data: UserCreateSchema):
        """Register a user using IP as an identifier."""

        return await database["users"].insert_one(data.model_dump())
        
    