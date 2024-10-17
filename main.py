from typing import Union
from fastapi import FastAPI
from contextlib import asynccontextmanager
from config.connection import prisma_connection
from app.middlewares.status_middleware import statusMiddleware
from app.middlewares.role_middleware import roleMiddleware
from app.auth.controller import auth
from app.todos.controller import todos
from app.admin.users.controller import users
from app.admin.users.role.controller import role
from app.admin.users.status.controller import status



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conectar a la base de datos al inicio
    await prisma_connection.connect()
    yield  # Aquí es donde la aplicación comienza a recibir solicitudes
    # Desconectar de la base de datos cuando la aplicación se apaga
    await prisma_connection.disconnect()
app = FastAPI(lifespan=lifespan)

app.add_middleware(statusMiddleware)
app.add_middleware(roleMiddleware)
app.include_router(auth)
app.include_router(todos)
app.include_router(users)
app.include_router(role)
app.include_router(status)
