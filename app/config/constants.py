import os

from fastapi.security import APIKeyHeader

JWT_SECRET = os.getenv("JWT_SECRET")
MONGO_URL = os.getenv("MONGO_URL")
ACCESS_TOKEN = APIKeyHeader(name="Authorization")

if not JWT_SECRET or not MONGO_URL:
    raise ValueError("Environment variables are not set correctly.")
