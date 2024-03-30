from datetime import datetime, timezone

from pydantic import BaseModel

from app.models.mongo import MongoModel

"""
Model DAO
"""


class UserInDAO(MongoModel):
    username: str
    email: str
    password: str
    dateCreated: datetime = datetime.now(timezone.utc)


class UserOutDAO(UserInDAO):
    id: str
    lastModified: datetime


class AuthenticatedUserOutDTO(BaseModel):
    id: str
    username: str
    email: str
    token: str
