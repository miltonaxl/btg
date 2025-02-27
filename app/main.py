"""
FastAPI entry point for the application.

This file is responsible for initializing the FastAPI application, registering middleware,
and including API routers. Specifically:
- The `UserCheckerMiddleware` is added to ensure each request contains a valid user IP and balance information.
- The `transactions` router is included to handle API routes related to financial transactions.

The application starts here, and routes are processed based on the request and middleware handling.
"""
from fastapi import FastAPI
from app.middlewares.ip_validation import IpValidationIfComing

from app.api.routers.routers import api_router

app = FastAPI()



app.add_middleware(IpValidationIfComing)

app.include_router(api_router, prefix="/api/v1")

