import os
from dotenv import load_dotenv
from passlib.context import CryptContext

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("HASH_PASSWORD_ALGORITHM")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashPassword(password:str)-> str:
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str)-> bool:
    return pwd_context.verify(plain_password, hashed_password)