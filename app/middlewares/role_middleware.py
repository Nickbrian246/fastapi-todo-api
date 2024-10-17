from fastapi import FastAPI ,Request, Response, HTTPException, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp
from ..auth.utils.jwt import decodeAccessToken
from ..decorators.handle_error_decorator import errorHandler
from config.connection import prisma_connection


class roleMiddleware(BaseHTTPMiddleware):
  def __init__(self, app: FastAPI) -> None:
    super().__init__(app)

  @errorHandler
  async def dispatch(self, request:Request, call_next) -> Response:
    path = request.url.path                   
    if not path.startswith("/admin"):
      response  = await call_next(request)
      return response
    
    jwt = request.headers.get("authorization")
    if not jwt:
      status_code=status.HTTP_401_UNAUTHORIZED
      content={"detail":"No JWT provided"}
      return JSONResponse(content=content, status_code=status_code)
    
    jwt_decoded = decodeAccessToken(jwt.split()[-1])
    user = await prisma_connection.prisma.user.find_first_or_raise(where={"id":int(jwt_decoded["id"])})
    
    if user.dict()["role"]  !="ADMIN":
      status_code=status.HTTP_401_UNAUTHORIZED
      content={"detail":"Only Admin users  can  access this content"}
      return JSONResponse(content=content, status_code=status_code)
    
    response  = await call_next(request)
    return response
  

