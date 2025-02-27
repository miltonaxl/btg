
"""API routes for managing financial user."""
from fastapi import APIRouter, Depends, HTTPException, Request
from app.domains.users.schemas import UserCreateSchema
from app.domains.users.use_cases import UserUseCases
from app.core.shared.decorators.validate_schemas import ValidateSchemas

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
async def register_user(request: Request,
                        
                        _: UserCreateSchema = Depends(ValidateSchemas(UserCreateSchema)),
                        use_case: UserUseCases = Depends()):
    """Create a new user."""
    data = await request.json()
    user_ip = request.state.user_ip
    
    data["ip"] = user_ip
    
    
   
        
    
    return await use_case.register_user(data)