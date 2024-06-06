from typing import Annotated

from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session


from crud.User import create_user, get_user_by_email
from utils import check_password_equality

from database.database import get_db
from schemas.auth import RegUser, LogUser, Token, User


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post('/send')
def auth_user(user: LogUser, db:Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user is  None:
        raise HTTPException(status_code=400, detail="Неправильный логин или пароль")
    if not check_password_equality(db_user.hashed_password, user.password):
        raise HTTPException(status_code=400, detail="Неправильный логин или пароль")
    if db_user.admin is not None:
        role_id = db_user.admin.id
        user_type='admin'
    elif  db_user.extranet is not None:
        role_id = db_user.extranet.id
        user_type='extranet'
    else:
        role_id = db_user.customer.id
        user_type='customer'
    
    return Token(username=db_user.username, user_role=user_type, role_id=role_id)


@router.post('/reg')
def register_user(user: RegUser, db:Session = Depends(get_db)) -> User:
    db_user = get_user_by_email(db, user.email)
    if db_user is not None:
        raise HTTPException(status_code=400, detail="Почта уже используется другим пользователем")
    
    return create_user(db, user)


