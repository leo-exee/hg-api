from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel, EmailStr

from app.models.mongo import MongoModel, PyObjectId

"""
Model DAO
"""


class UserInDAO(MongoModel):
    username: str
    email: EmailStr
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
