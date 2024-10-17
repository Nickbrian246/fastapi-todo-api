from pydantic import BaseModel
from typing import List

class UsersToUpdate(BaseModel):
    users: List[str]
