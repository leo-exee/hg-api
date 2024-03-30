from fastapi import APIRouter, Depends

from app.models.mongo import PyObjectId
from app.models.toilet import ToiletInDAO
from app.models.user import UserOutDAO
from app.services.token_service import get_token_user_service, validate_token_service

user_controller = APIRouter(
    prefix="/user",
    tags=["user"],
    dependencies=[Depends(get_token_user_service)],
)


@user_controller.get(
    "",
    summary="Get user info",
    description="Get user info",
)
async def get_user_info(user: UserOutDAO = Depends(get_token_user_service)):
    return user


@user_controller.patch(
    "",
    summary="Update user info",
    description="Update user info",
)
async def update_user_info(user: UserOutDAO = Depends(get_token_user_service)):
    return user


@user_controller.delete(
    "",
    summary="Delete user",
    description="Delete user",
)
async def delete_user(user: UserOutDAO = Depends(get_token_user_service)):
    return user
