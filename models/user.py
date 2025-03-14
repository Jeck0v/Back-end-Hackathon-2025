from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: str
    username: str
    firstname: str
    name: str
    email: EmailStr
    password: str
    role: Optional[str] = "user"

class UserResponse(BaseModel):
    id: str
    username: str
    firstname: str
    name: str
    email: EmailStr
    role: Optional[str] = "user"
    class Config:
        orm_mode = True
class UserInDB(User):
    hashed_password: str

