from datetime import datetime

from pydantic import BaseModel


class TokenInDAO(BaseModel):
    userId: str
    token: str
    dateCreated: datetime


class TokenOutDAO(TokenInDAO):
    id: str
    lastModified: datetime


class JWTTokenModelInDTO(BaseModel):
    userId: str
    isAdmin: bool
    dateCreated: datetime
