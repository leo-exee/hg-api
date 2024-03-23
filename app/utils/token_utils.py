import jwt

from app.constants import JWT_SECRET


def encode_token(payload) -> str:
    return jwt.encode(dict(payload), JWT_SECRET, algorithm="HS256")


def decode_token(encoded: str) -> dict:
    return jwt.decode(encoded, JWT_SECRET, algorithms=["HS256"])
