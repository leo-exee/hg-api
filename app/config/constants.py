import os

from fastapi.security import APIKeyHeader

JWT_SECRET = os.getenv("JWT_SECRET")
MONGODB_URL = os.getenv("MONGODB_URL")
ACCESS_TOKEN = APIKeyHeader(name="Authorization")

if not JWT_SECRET or not MONGODB_URL:
    raise ValueError("Environment variables are not set correctly.")
