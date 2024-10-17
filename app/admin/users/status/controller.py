from fastapi import APIRouter, Depends
from ....auth.utils.jwt import get_current_user
from ....auth.schemas.jwt_schema import DecodedToken
from ..schemas.users_to_update_schema import UsersToUpdate
from .service import update_status_to_block,update_status_to_unlock

status= APIRouter(prefix="/admin/users/status")

@status.patch("/block")
async def update_user_status_to_block(
  users_list:UsersToUpdate,
  user:DecodedToken= Depends(get_current_user)
  ):
  return  await update_status_to_block(users_list)

@status.patch("/unlock")
async def update_user_status_to_unlock(
  users_list:UsersToUpdate,
  user:DecodedToken= Depends(get_current_user)
  ):
  return await update_status_to_unlock(users_list)




