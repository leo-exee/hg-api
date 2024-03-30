import jwt

from app.constants import JWT_SECRET
from app.models.authentification import JWTTokenModelInDTO


def encode_token(payload: JWTTokenModelInDTO) -> str:
    return jwt.encode(dict(payload), JWT_SECRET, algorithm="HS256")


def decode_token(encoded: str) -> dict:
    return jwt.decode(encoded, JWT_SECRET, algorithms=["HS256"])
