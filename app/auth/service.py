import json
from .schemas.auth_schema import Signin,SignUpUser
from .utils.password import verify_password,hashPassword
from .utils.jwt import create_access_token,decodeAccessToken
from ..app_schemas.api_success_response_schema import ApiSuccessResponseAccessToken,ApiSuccessResponseWithMetaData
from config.connection import prisma_connection
from .utils.error_handler_decorator import authErrorHandler
from fastapi import HTTPException, status


@authErrorHandler
async def signupUser (userCredentials:SignUpUser)->ApiSuccessResponseAccessToken:
    hashedPassword = hashPassword(userCredentials.password)
    data = await  prisma_connection.prisma.user.create({
      "email":userCredentials.email,
      "password":hashedPassword,
      "name":userCredentials.name,
      "familyName":userCredentials.familyName,
      "ToDos":json.dumps([])})
    
    accessToken = create_access_token({"id":data.id,"email":data.email})
    return {'access_token':accessToken}
    

@authErrorHandler
async def signinUser (userCredentials:Signin)->ApiSuccessResponseAccessToken:
    print({"email":userCredentials.email, "password":userCredentials.password})
    userInDB = await  prisma_connection.prisma.user.find_unique_or_raise({"email":userCredentials.email})

    decodedPassword = verify_password(userCredentials.password,userInDB.password)
    if not decodedPassword:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    
    accessToken = create_access_token({"id":userInDB.id,"email":userInDB.email})
    return {"access_token":accessToken}
    
