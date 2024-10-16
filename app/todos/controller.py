from fastapi import APIRouter, Depends
from ..auth.utils.jwt import get_current_user
from .schemas.todos_schema import To_dos_list
todos = APIRouter(prefix="/todos")

@todos.put("/")
async def update_to_dos(todos:To_dos_list, user:dict = Depends(get_current_user)):
  print (user)
  return "hola "
  # return await  signinUser(userCredentials)

