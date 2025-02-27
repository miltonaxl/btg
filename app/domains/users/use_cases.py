"""
Specific use cases for users identified by IP.
"""
from app.domains.users.service import UserService
from app.domains.users.schemas import UserCreateSchema

class UserUseCases:
    """Use cases for managing users identified by IP."""
    
    async def register_user(self, data: UserCreateSchema):
        """Use case: Identify user by IP and register if necessary."""
        return await UserService().register_user(data)
    
    async def get_user_by_ip(self, user_ip: str):
        """Use case: Retrieve user by IP."""
        return await UserService().get_user_by_ip(user_ip)
    
    async def get_by_id(self, user_id: str):
        """Use case: Retrieve user by ID."""
        return await UserService().get_by_id(user_id)
