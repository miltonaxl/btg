"""
UserCheckerMiddleware: Middleware to validate ip coming from the request.
"""

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from app.domains.users.use_cases import UserUseCases
from app.domains.balances.use_cases import BalanceUseCases

class IpValidationIfComing(BaseHTTPMiddleware):
    """ 
    Middleware to validate ip coming from the request.
    
    """

    async def dispatch(self, request: Request, call_next):
        """
        Intercept the request and validate the user IP.

        Parameters:
        - request: The incoming HTTP request that contains user-related information (e.g., IP address).
        - call_next: A function that processes the request and returns a response.

        Returns:
        - JSONResponse: A JSON response with an error message or the normal response from the next handler.
        """
        ip = request.headers.get("X-Forwarded-For", request.client.host)
        if not ip:
            return JSONResponse(status_code=400, content={"error": "User IP not found in request."})
            
            
        user = await UserUseCases().get_user_by_ip(ip)
        
        request.state.user = user
        request.state.user_ip = ip

        response = await call_next(request)
        return response
