"""
Business logic for users identified by IP.
"""
from app.domains.users.repository import UserRepository
from app.domains.users.schemas import UserCreateSchema
from app.domains.balances.use_cases import BalanceUseCases

from app.domains.users.models import UserModel
class UserService:
    """Handles business logic for users based on IP."""
    
    def __init__(self):
        self.balance_use_case = BalanceUseCases()
        self.user_repository = UserRepository()
    
    async def register_user(self, data: UserCreateSchema):
        """Retrieve or register a user based on IP."""
        
        
        user = await self.user_repository.get_by_email(data.get("email"))
        
        if user:
            return user
        
        user_model = UserModel(**data)
        
        print(" DATA => ", user_model)
        
        
        data_serializer = UserCreateSchema(
            **data
        )
        
        
        
        
        user_created = await UserRepository.register_user(data_serializer)
        
        user_id = user_created.inserted_id
        
        await self.balance_use_case.create_balance(user_id)
        return await self.get_user_by_ip(data.get("ip"))
    
    async def get_user_by_ip(self, user_ip: str):
        """Retrieve a user based on IP."""
        return await self.user_repository.get_by_ip(user_ip)
    
    async def get_by_id(self, user_id: str):
        """Retrieve a user by ID."""
        return await self.user_repository.get_by_id(user_id)