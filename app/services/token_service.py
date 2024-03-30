from datetime import datetime, timezone

from fastapi import status

from app.config.error_model import ErrorResponse
from app.models.authentification import JWTTokenModelInDTO, TokenInDAO, TokenOutDAO
from app.models.mongo import PyObjectId
from app.repositories.token_repository import create_token
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
