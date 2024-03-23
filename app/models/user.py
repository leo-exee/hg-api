from datetime import datetime, timezone

from pydantic import BaseModel

"""
Model DAO
"""


class UserInDAO(BaseModel):
    username: str
    email: str
    password: str
    dateCreated: datetime = datetime.now(timezone.utc)


class UserOutDAO(UserInDAO):
    id: str
    lastModified: datetime


"""
Model DTO
"""


class AuthUserOutDTO(UserOutDAO):
    token: str
