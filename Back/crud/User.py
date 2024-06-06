from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from schemas.auth import RegUser
from database import models
from utils import hash_password


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_all_user(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: RegUser):
    hashed_password = hash_password(user.password)
    user_db = models.User(email=user.email, username=user.username, hashed_password=hashed_password)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db


def create_admin(db: Session, user: RegUser):
    user_db = create_user(db,user)
    new_admin = models.Admin(user_id=user_db.id)
    
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return  new_admin.user


def create_extranet(db:Session, user:RegUser):
    user_db = create_user(db,user)
    new_extranet = models.Extranet(user_id=user_db.id)
    
    db.add(new_extranet)
    db.commit()
    db.refresh(new_extranet)
    return  new_extranet.user


def create_customer(db: Session, user: RegUser):
    user_db = create_user(db,user)
    new_customer = models.Customer(user_id=user_db.id)

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return  new_customer.user