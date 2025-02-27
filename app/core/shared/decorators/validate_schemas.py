""" Decorator to validate schemas """

from fastapi import HTTPException, Request, Depends
from pydantic import ValidationError

class ValidateSchemas:
    """
    Dependency class for validating request data against a given Pydantic schema.

    This class ensures that incoming request data adheres to the specified schema,
    raising an HTTPException if validation fails.
    """

    def __init__(self, schema):
        """
        Initialize with the Pydantic schema to validate against.
        
        :param schema: The Pydantic schema class used for validation.
        """
        self.schema = schema

    async def __call__(self, request: Request):
        """
        Asynchronously validates the request data against the schema.
        
        :param request: The incoming FastAPI request object.
        :return: An instance of the validated schema.
        :raises HTTPException: If validation fails.
        """
        try:
            data = await request.json()
            
            if not request.state.user:
                return self.schema(**data)
            user_id = request.state.user.id
            data["user_id"] = user_id
            
            return self.schema(**data)
        except ValidationError as e:
            raise HTTPException(status_code=422, detail=e.errors())