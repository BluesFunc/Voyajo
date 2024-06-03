from pydantic import BaseModel, EmailStr

class BaseUser(BaseModel):
    username: str


class LogUser(BaseModel):
    email: str
    password: str
        

class RegUser(LogUser):
    email: str
    

class UserCreate(BaseUser):
    hashed_password: str
    email: str
  
class Token(BaseModel):
    token: str
    token_type: str  
    
class User(UserCreate):
    id: int
    
    class Config:
        from_attributes = True
