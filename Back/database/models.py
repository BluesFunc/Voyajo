from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import EmailType

from .database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)

    email = Column(EmailType, index=True)
    username = Column(String)
    hashed_password = Column(String)


    