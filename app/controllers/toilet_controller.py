from fastapi import APIRouter, Depends

from app.models.mongo import PyObjectId
from app.models.toilet import Review, ToiletInDAO, ToiletOutDAO
from app.models.user import UserOutDAO
from app.services.toilet_service import (
    create_toilet_review_service,
    create_toilet_service,
    delete_toilet_review_service,
    delete_toilet_service,
    get_toilet_by_id_service,
    get_toilets_details_service,
    update_toilet_review_service,
    update_toilet_service,
)
from app.services.token_service import get_token_user_service, validate_token_service

toilet_controller = APIRouter(prefix="/toilets", tags=["toilets"])

user_toilet_controller = APIRouter(
    prefix="/toilets",
    tags=["toilets"],
    dependencies=[Depends(validate_token_service), Depends(get_token_user_service)],
)


@toilet_controller.get(
    "/",
    summary="Get all toilets",
    description="Get all toilets",
)
async def get_toilets():
    return await get_toilets_details_service()


@toilet_controller.get(
    "/{toilet_id}",
    summary="Get toilet by id",
    description="Get toilet by id",
)
async def get_toilet_by_id(toilet_id: PyObjectId):
    return await get_toilet_by_id_service(toilet_id)


@user_toilet_controller.post(
    "/",
    summary="Create toilet",
    description="Create toilet",
    response_model=ToiletOutDAO,
)
async def create_toilet(
    toilet: ToiletInDAO,
    user: UserOutDAO = Depends(get_token_user_service),
) -> ToiletOutDAO:
    return await create_toilet_service(toilet, user.id)


@user_toilet_controller.patch(
    "/{toilet_id}",
    summary="Update toilet",
    description="Update toilet",
)
async def update_toilet(
    toilet_id: PyObjectId,
    toilet: ToiletInDAO,
    user: UserOutDAO = Depends(get_token_user_service),
):
    return await update_toilet_service(toilet_id, toilet, user.id)


@user_toilet_controller.delete(
    "/{toilet_id}",
    summary="Delete toilet",
    description="Delete toilet",
)
async def delete_toilet(
    toilet_id: PyObjectId,
    user: UserOutDAO = Depends(get_token_user_service),
):
    return await delete_toilet_service(toilet_id, user.id)


@user_toilet_controller.post(
    "/{toilet_id}/reviews",
    summary="Create review",
    description="Create review",
)
async def create_review(
    toilet_id: PyObjectId,
    review: Review,
    user: UserOutDAO = Depends(get_token_user_service),
):
    return await create_toilet_review_service(toilet_id, review, user.id)


@user_toilet_controller.patch(
    "/{toilet_id}/reviews/{review_id}",
    summary="Update review",
    description="Update review",
)
async def update_review(
    toilet_id: PyObjectId,
    review: Review,
    user: UserOutDAO = Depends(get_token_user_service),
):
    return await update_toilet_review_service(toilet_id, review, user.id)


@user_toilet_controller.delete(
    "/{toilet_id}/reviews/{review_id}",
    summary="Delete review",
    description="Delete review",
)
async def delete_review(
    toilet_id: PyObjectId,
    user: UserOutDAO = Depends(get_token_user_service),
):
    return await delete_toilet_review_service(toilet_id, user.id)
