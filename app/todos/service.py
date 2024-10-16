from config.connection import prisma_connection
from app.decorators.handle_error_decorator import errorHandler
from .schemas.todos_schema import To_dos_list


@errorHandler
async def update_to_dos(todos:To_dos_list):
  pass