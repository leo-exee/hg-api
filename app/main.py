from fastapi import FastAPI

from app.config.database import close_mongo_connection, connect_to_mongo
from app.hg_api import hg_api

app = FastAPI(
    title="HG - API",
    description=("API for HG project"),
    version="2.0.0",
    redoc_url="/swagger",
    docs_url="/docs",
)
app.mount("/", hg_api)


@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()


@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()
