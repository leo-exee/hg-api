from datetime import datetime

from pydantic import BaseModel

from app.models.mongo import MongoModel


class TokenInDAO(MongoModel):
    userId: str
    token: str
    dateCreated: datetime


class TokenOutDAO(TokenInDAO):
    id: str


class JWTTokenModelInDTO(BaseModel):
    userId: str
    isAdmin: bool
    dateCreated: datetime


class AuthentificationInDTO(BaseModel):
    email: str
    password: str
