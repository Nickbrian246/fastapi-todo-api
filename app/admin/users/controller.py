from fastapi import APIRouter, Depends
from ...auth.utils.jwt import get_current_user
from ...auth.schemas.jwt_schema import DecodedToken
from .service import  get_all_users, get_user_by_id, delete_user as user_delete
users = APIRouter(prefix="/admin/users")

@users.get("")
async def get_users( user:DecodedToken= Depends(get_current_user)):
  return await get_all_users()

@users.get("/{id}")
async def get_user(id:str,user:DecodedToken= Depends(get_current_user)):
  return await get_user_by_id(int(id))

@users.delete("/{id}")
async def delete_user(id:str):
  return await  user_delete(id)

