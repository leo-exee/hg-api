from fastapi import APIRouter, status

from app.models.authentification import AuthentificationInDTO
from app.models.user import AuthenticatedUserOutDTO, UserInDAO
from app.services.user_service import (
    login_user_service,
    register_user_service,
)

auth_controller = APIRouter(prefix="/auth", tags=["auth"])


@auth_controller.post(
    "/register",
    response_model=AuthenticatedUserOutDTO,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    description="Register a new user",
    responses={status.HTTP_201_CREATED: {"description": "User created"}},
)
async def register(user: UserInDAO):
    return await register_user_service(user)


@auth_controller.post(
    "/login",
    response_model=AuthenticatedUserOutDTO,
    status_code=status.HTTP_200_OK,
    summary="Login",
    description="Login",
)
async def login(payload: AuthentificationInDTO):
    return await login_user_service(payload.email, payload.password)
