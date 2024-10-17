from fastapi import APIRouter, Depends
from ..auth.utils.jwt import get_current_user
from .schemas.todos_schema import To_dos_list
from ..app_schemas.jwt_decoded_schema import DecodedToken
from .service import update_user_to_dos
todos = APIRouter(prefix="/todos")

@todos.put("")
async def update_to_dos(
  todos:To_dos_list,
  user:DecodedToken = Depends(get_current_user)
  ):
  print(user)
  return await  update_user_to_dos(todos, user)

