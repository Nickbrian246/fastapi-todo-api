from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv
from jwt.exceptions import InvalidTokenError
from ..schemas.jwt_schema import DecodedToken

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("HASH_PASSWORD_ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = 3000
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decodeAccessToken(token:str)-> DecodedToken:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload


def get_current_user(token: str = Depends(oauth2_scheme))->DecodedToken:
    try:
        payload = decodeAccessToken(token)
        return payload 
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )