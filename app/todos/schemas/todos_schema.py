from pydantic import BaseModel,EmailStr, Field 
from typing import List
class ToDo(BaseModel):
  toDoId:str
  name:str
  status:bool
  label:str 

class To_dos_list(BaseModel):
  toDos:List[ToDo] 


