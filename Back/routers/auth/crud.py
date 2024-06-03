from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session


from schemas.auth import RegUser
from database import models
from .utils import hash_password



def get_user_by_username(db: Session, username:str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str): 
    return db.query(models.User).filter(models.User.email == email).first()


    
def create_user(db: Session, user: RegUser ):
    hashed_password = hash_password(user.password)
    user_db = models.User(email=user.email,username =user.username ,hashed_password=hashed_password )
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

