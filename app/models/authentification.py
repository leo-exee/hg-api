from datetime import datetime

from pydantic import BaseModel

from app.models.mongo import MongoModel, PyObjectId


class TokenInDAO(MongoModel):
    userId: PyObjectId
    token: str
    dateCreated: datetime


class TokenOutDAO(TokenInDAO):
    id: PyObjectId


class JWTTokenModelInDTO(BaseModel):
    userId: str
    isAdmin: bool
    dateCreated: str


class AuthentificationInDTO(BaseModel):
    email: str
    password: str
