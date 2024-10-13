from pydantic import BaseModel,EmailStr, Field 
class SignUpUser(BaseModel):
  name: str
  familyName:str
  email: EmailStr
  password:str = Field(..., min_length=8)

class Signin(BaseModel):
  email:EmailStr
  password:str = Field(..., min_length=8)