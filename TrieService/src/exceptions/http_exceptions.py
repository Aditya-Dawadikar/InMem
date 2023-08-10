from fastapi import FastAPI, HTTPException, status
from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse

class InmemHTTPException(HTTPException):
    def __init__(self,
                status_code: int,
                message:str,
                success:bool,
                data):
        self.status_code = status_code
        self.message = message
        self.success = success
        self.data = data
        
        super().__init__(status_code=status_code,detail=message)

class InternalServerErrorException(InmemHTTPException):
    def __init__(self, data):
        super().__init__(status_code=500,
                         message="Internal Server Error",
                         success=False,
                         data=data)

class ResourceNotFoundException(InmemHTTPException):
    def __init__(self, data):
        super().__init__(status_code=404,
                         message="Resource Not Found",
                         success=False,
                         data=data)

class ForbiddenException(InmemHTTPException):
    def __init__(self, data):
        super().__init__(status_code=403,
                         message="Forbidden",
                         success=False,
                         data=data)

class UnauthorizedException(InmemHTTPException):
    def __init__(self, data):
        super().__init__(status_code=401,
                         message="Unauthorized User",
                         success=False,
                         data=data)

class BadRequestException(InmemHTTPException):
    def __init__(self, data):
        super().__init__(status_code=400,
                         message="Bad Request",
                         success=False,
                         data=data)

class ConflictException(InmemHTTPException):
    def __init__(self, data):
        super().__init__(status_code=409,
                         message="Conflict",
                         success=False,
                         data=data)


def add_http_exception_handlers(_app:FastAPI):
    @_app.exception_handler(InmemHTTPException)
    async def http_exception_handler(req: Request, exception: InmemHTTPException):
        return JSONResponse(
            status_code = exception.status_code,
            content={
                "success": exception.success,
                "message": exception.message,
                "data": exception.data
            }
        )
