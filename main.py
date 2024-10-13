from typing import Union
from fastapi import FastAPI
from contextlib import asynccontextmanager
from  app.auth.controller import auth
from config.connection import prisma_connection


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conectar a la base de datos al inicio
    await prisma_connection.connect()
    yield  # Aquí es donde la aplicación comienza a recibir solicitudes
    # Desconectar de la base de datos cuando la aplicación se apaga
    await prisma_connection.disconnect()
app = FastAPI(lifespan=lifespan)
app.include_router(auth)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}