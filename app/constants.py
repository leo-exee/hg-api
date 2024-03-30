import os

JWT_SECRET = os.getenv("JWT_SECRET")
MONGO_URL = os.getenv("MONGO_URL")

if not JWT_SECRET or not MONGO_URL:
    raise ValueError("Environment variables are not set correctly.")
