from datetime import datetime

from pydantic import BaseModel


class JWTTokenModelInDTO(BaseModel):
    userId: str
    isAdmin: bool
    dateCreated: datetime
