from fastapi import APIRouter

from app.models.authentification import AuthentificationInDTO
from app.models.user import AuthenticatedUserOutDTO, UserInDAO
from app.services.user_service import login_user_service, register_user_service

auth_controller = APIRouter(prefix="/auth", tags=["auth"])


@auth_controller.post(
    "/register",
    response_model=AuthenticatedUserOutDTO,
    summary="Register a new user",
    description="Register a new user",
)
async def register(user: UserInDAO):
    return register_user_service(user)


@auth_controller.post(
    "/login",
    response_model=AuthenticatedUserOutDTO,
    summary="Login",
    description="Login",
)
async def login(payload: AuthentificationInDTO):
    return login_user_service(payload.email, payload.password)
