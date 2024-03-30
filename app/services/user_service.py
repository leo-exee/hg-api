from fastapi import status

from app.config.error_model import ErrorResponse
from app.models.user import AuthenticatedUserOutDTO, UserInDAO
from app.repositories.token_repository import get_token
from app.repositories.user_repository import create_user, get_user_by_auth
from app.services.token_service import create_token_service
from app.utils.user_utils import get_password_hash, verify_password


async def register_user_service(user: UserInDAO) -> AuthenticatedUserOutDTO:
    user.password = get_password_hash(user.password)
    new_user = await create_user(user)
    if not new_user:
        raise ErrorResponse(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "Error creating user",
            "INTERNAL_SERVER_ERROR",
        )
    token = await create_token_service(
        new_user.id,
    )
    return AuthenticatedUserOutDTO(**new_user.dict(), token=token.token)


async def login_user_service(email: str, password: str) -> AuthenticatedUserOutDTO:
    user = await get_user_by_auth(email)
    if not user:
        raise ErrorResponse(
            status.HTTP_404_NOT_FOUND,
            "User not found",
            "USER_NOT_FOUND",
        )
    if not verify_password(password, user.password):
        raise ErrorResponse(
            status.HTTP_401_UNAUTHORIZED,
            "Incorrect password",
            "INCORRECT_PASSWORD",
        )
    token = await get_token(user.id)
    if not token:
        token = await create_token_service(user.id)
    return AuthenticatedUserOutDTO(**user.dict(), token=token.token)
