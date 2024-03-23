from fastapi import FastAPI

from app.hg_api import hg_api

app = FastAPI(
    title="HG - API",
    description=("API for HG project"),
    version="2.0.0",
    redoc_url="/swagger",
    docs_url="/docs",
)
app.mount("/", hg_api)
