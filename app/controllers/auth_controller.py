from fastapi import APIRouter, Response, status

from app.models.authentification import AuthentificationInDTO
from app.models.user import AuthenticatedUserOutDTO, UserInDAO
from app.services.user_service import (
    login_user_service,
    register_user_service,
    user_exists_service,
)

auth_controller = APIRouter(prefix="/auth", tags=["auth"])


@auth_controller.post(
    "/register",
    response_model=AuthenticatedUserOutDTO,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    description="Register a new user",
)
async def register(user: UserInDAO, response: Response):
    if user_exists := await user_exists_service(user.email, user.password):
        response.status_code = status.HTTP_202_ACCEPTED
        return user_exists
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
