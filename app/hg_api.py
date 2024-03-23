from typing import Union
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import status


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


class ErrorResponse(Exception):
    def __init__(
        self,
        code: Union[str, int],
        message: str,
        status: str,
        details: list[object] | None = None,
    ) -> None:
        self.code = code
        self.message = message
        self.status = status
        self.details = details if details is not None else []

    @classmethod
    def from_error(cls, e: Union["ErrorResponse", Exception]) -> "ErrorResponse":
        if isinstance(e, cls):
            return e
        return cls(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "Internal Server Error",
            "INTERNAL_SERVER_ERROR",
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


@hg_api.exception_handler(Exception)
def exception_handler(request: Request, exc: ErrorResponse) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=format_error_response(exc.code, exc.message, exc.status, exc.details),
    )
