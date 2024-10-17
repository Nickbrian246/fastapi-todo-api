import asyncio
from config.connection import prisma_connection
from ....decorators.handle_error_decorator import errorHandler
from ..schemas.users_to_update_schema import UsersToUpdate


@errorHandler
async def update_status_to_block(users_list: UsersToUpdate):
    return  await asyncio.gather(
        *[update_user_status(user_id, 'BLOCK') for user_id in users_list.users],
        return_exceptions=True)

@errorHandler
async def update_status_to_unlock(users_list: UsersToUpdate):
    return await asyncio.gather(
        *[update_user_status(user_id, 'ACTIVE') for user_id in users_list.users]
        ,return_exceptions=True)

async def update_user_status(user_id: str, role: str):
    return await prisma_connection.prisma.user.update(
        where={'id': int(user_id)},
        data={'status': role}
    )