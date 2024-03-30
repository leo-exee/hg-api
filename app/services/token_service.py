from datetime import datetime, timezone

from fastapi import Security, status

from app.config.constants import ACCESS_TOKEN
from app.config.error_model import ErrorResponse
from app.models.authentification import JWTTokenModelInDTO, TokenInDAO, TokenOutDAO
from app.models.mongo import PyObjectId
from app.models.user import UserOutDAO
from app.repositories.token_repository import (
    create_token,
    get_token,
)
from app.repositories.user_repository import get_user
from app.utils.token_utils import encode_token


async def create_token_service(
    userId: PyObjectId,
) -> TokenOutDAO:
    token = encode_token(
        JWTTokenModelInDTO(
            userId=str(userId),
            isAdmin=False,
            dateCreated=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        )
    )

    response = await create_token(
        TokenInDAO(token=token, userId=userId, dateCreated=datetime.now(timezone.utc))
    )
    if not response:
        raise ErrorResponse(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "Error creating token",
            "INTERNAL_SERVER_ERROR",
        )
    return response


async def validate_token_service(
    token: str | None = Security(ACCESS_TOKEN),
) -> TokenOutDAO:
    if not token:
        raise ErrorResponse(
            status.HTTP_401_UNAUTHORIZED,
            "Token is missing",
            "TOKEN_MISSING",
        )
    valid_token = await get_token(token)
    if not valid_token:
        raise ErrorResponse(
            status.HTTP_401_UNAUTHORIZED,
            "Invalid token",
            "INVALID_TOKEN",
        )
    return valid_token


async def get_token_user_service(
    token: str | None = Security(ACCESS_TOKEN),
) -> UserOutDAO:
    valid_token = await validate_token_service(token)
    user = await get_user(valid_token.userId)
    if not user:
        raise ErrorResponse(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "Error getting user",
            "INTERNAL_SERVER_ERROR",
        )
    return user
