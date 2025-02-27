""" Middleware for request validation before hitting specific endpoints. """

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.domains.users.use_cases import UserUseCases

async def validate_request(request: Request):
    """Middleware for request validation before hitting specific endpoints."""
    
    ip = request.headers.get("X-Forwarded-For", request.client.host)
    if not ip:
         raise HTTPException(status_code=400, detail="User IP not found.")
        
        
    user = await UserUseCases().get_user_by_ip(ip)
    
    if not user:
        raise HTTPException(status_code=400, detail= "Unauthorized user.")
    
    return request