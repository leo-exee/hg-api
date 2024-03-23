import os

import mysql.connector

JWT_SECRET = os.getenv("JWT_SECRET")
HOST = os.getenv("HOST")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")

if not JWT_SECRET or not HOST or not USERNAME or not PASSWORD or not DATABASE:
    raise ValueError("Environment variables are not set correctly.")

DB = mysql.connector.connect(
    host=HOST, user=USERNAME, password=PASSWORD, database=DATABASE
)
