from fastapi import FastAPI ,Request, Response, HTTPException, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction
from starlette.types import ASGIApp
from ..auth.utils.jwt import decodeAccessToken
from ..decorators.handle_error_decorator import errorHandler


class DecodeJwtMiddleware(BaseHTTPMiddleware):
  def __init__(self, app: FastAPI) -> None:
    super().__init__(app)

  @errorHandler
  async def dispatch(self, request:Request, call_next) -> Response:
    path = request.url.path #/auth/signin , /auth/signup  if match => continue
    print(path)                  
    # if path =="/auth/signin" or path == "/auth/signup":
    #   response  = await call_next(request)
    #   return response 

    jwt = request.headers.get("authorization")
    if not jwt:
      status_code=status.HTTP_401_UNAUTHORIZED
      content={"detail":"No JWT provided"}
      return JSONResponse(content=content, status_code=status_code)
    
    jwt_decoded = decodeAccessToken(jwt.split()[-1])
    request.state.user = jwt_decoded
    print(request.state.user,"user object")

    response  = await call_next(request)
    return response