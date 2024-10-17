import json
from prisma.models import User
from config.connection import prisma_connection
from app.decorators.handle_error_decorator import errorHandler
from .schemas.todos_schema import To_dos_list
from ..app_schemas.jwt_decoded_schema import DecodedToken
from ..app_schemas.api_success_response_schema import ApiSuccessResponse

@errorHandler
async def update_user_to_dos(todos:To_dos_list, user:DecodedToken)->ApiSuccessResponse[User]:
  data= await prisma_connection.prisma.user.update(
    where={"id":int(user['id'])},
    data={'ToDos':json.dumps(todos.dict()["toDos"])},

    )

  return {"data":data}