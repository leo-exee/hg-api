from typing import Union

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config.error_model import ErrorResponse
from app.controllers.auth_controller import auth_controller
from app.controllers.toilet_controller import toilet_controller

hg_api = FastAPI(
    title="HG - API",
    description=("API for HG project"),
    version="1.0.0",
    redoc_url="/swagger",
)

hg_api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def format_error_response(
    code: Union[str, int],
    message: str,
    status: str,
    details: list[object] | None = None,
) -> object:
    return {
        "error": {
            "code": code,
            "message": message,
            "status": status,
            "details": jsonable_encoder(details),
        }
    }


@hg_api.exception_handler(ErrorResponse)
def exception_handler(request: Request, exc: ErrorResponse) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=format_error_response(exc.code, exc.message, exc.status, exc.details),
    )


"""
ROUTER
"""
hg_api.include_router(auth_controller)
hg_api.include_router(toilet_controller)
