from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    username: str


class LogUser(BaseModel):
    email: str
    password: str


class RegUser(LogUser):
    username: str


class UserCreate(BaseUser):
    hashed_password: str
    email: str


class Token(BaseModel):
    username: str
    user_role: str
    role_id: int

class User(UserCreate):
    id: int





    


