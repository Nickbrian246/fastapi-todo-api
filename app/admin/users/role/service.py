import asyncio
from config.connection import prisma_connection
from ....decorators.handle_error_decorator import errorHandler
from .role_schemas.users_to_update_schema import UsersToUpdate


@errorHandler
async def update_roles_to_admin(users_list: UsersToUpdate):
    return await asyncio.gather(
        *[update_user_role(user_id, 'ADMIN') for user_id in users_list.users])

@errorHandler
async def update_roles_to_user(users_list: UsersToUpdate):
   return  await asyncio.gather(
        *[update_user_role(user_id, 'USER') for user_id in users_list.users]
        ,return_exceptions=True)

async def update_user_role(user_id: str, role: str):
    return await prisma_connection.prisma.user.update(
        where={'id': int(user_id)},
        data={'role': role}
    )