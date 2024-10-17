from typing import List
from prisma import Prisma
from config.connection import prisma_connection
from ...auth.schemas.jwt_schema import DecodedToken
from ...decorators.handle_error_decorator import errorHandler
from ...app_schemas.api_success_response_schema import ApiSuccessResponse

@errorHandler
async def get_all_users()-> ApiSuccessResponse:
  users = await prisma_connection.prisma.user.find_many()
  return {"data": users}
  

@errorHandler
async def get_user_by_id(id:int):
  user =  await prisma_connection.prisma.user.find_first_or_raise(where={"id":id})
  return {"data":user}


@errorHandler
async def delete_user(id:str):
  user =  await prisma_connection.prisma.user.delete(where={"id":id})
  return {"data":user}
