import jwt

from app.config.constants import JWT_SECRET
from app.models.authentification import JWTTokenModelInDTO


def encode_token(payload: JWTTokenModelInDTO) -> str:
    return jwt.encode(dict(payload), JWT_SECRET, algorithm="HS256")
