from fastapi import APIRouter
from .service import signupUser,signinUser
from .schemas.auth_schema import SignUpUser, Signin
auth = APIRouter()

@auth.post("/auth/signin")
async def signin(userCredentials:Signin):
  return await  signinUser(userCredentials)

@auth.post("/auth/signup")
async def signup(userCredentials:SignUpUser):
  return await  signupUser(userCredentials)