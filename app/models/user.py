from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel

from app.models.mongo import MongoModel, PyObjectId

"""
Model DAO
"""


class UserInDAO(MongoModel):
    username: str
    email: str
    password: str
    dateCreated: datetime | None
    lastModified: datetime | None


class UserOutDAO(UserInDAO):
    id: PyObjectId


class AuthenticatedUserOutDTO(BaseModel):
    id: PyObjectId
    username: str
    email: str
    token: str

    class Config:
        json_encoders = {ObjectId: str}
