from fastapi import APIRouter, Depends
from ....auth.utils.jwt import get_current_user
from ....auth.schemas.jwt_schema import DecodedToken
from .service import update_roles_to_admin,update_roles_to_user
from .role_schemas.users_to_update_schema import UsersToUpdate

role= APIRouter(prefix="/admin/users/role")

@role.patch("/user")
async def update_role_to_user(
  users_list:UsersToUpdate,
  user:DecodedToken= Depends(get_current_user)
  ):
  return await update_roles_to_user(users_list)



@role.patch("/admin")
async def update_role_to_admin(
  users_list:UsersToUpdate,
  user:DecodedToken= Depends(get_current_user)
  ):
  return await update_roles_to_admin(users_list)




