from fastapi import APIRouter

from app.models.user import AuthUserOutDTO, UserInDAO
from app.services.user_service import register_user_service

auth_controller = APIRouter(prefix="/auth", tags=["auth"])


@auth_controller.post(
    "/register",
    response_model=AuthUserOutDTO,
    summary="Register a new user",
    description="Register a new user",
)
def register(user: UserInDAO):
    return register_user_service(user)
