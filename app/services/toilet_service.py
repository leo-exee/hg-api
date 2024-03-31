from fastapi import status

from app.config.error_model import ErrorResponse
from app.models.mongo import PyObjectId
from app.models.toilet import Review, ToiletInDAO
from app.repositories.toilet_repository import (
    create_toilet,
    create_toilet_review,
    delete_toilet,
    delete_toilet_review,
    get_toilet_by_id,
    get_toilets_details,
    update_toilet,
    update_toilet_review,
)


async def get_toilets_details_service():
    return await get_toilets_details()


async def get_toilet_by_id_service(toilet_id: PyObjectId):
    toilet = await get_toilet_by_id(toilet_id)
    if not toilet:
        raise ErrorResponse(status.HTTP_404_NOT_FOUND, "Toilet not found", "NOT_FOUND")


async def get_toilet_reviews_service(toilet_id: PyObjectId):
    toilet = await get_toilet_by_id(toilet_id)
    if not toilet:
        raise ErrorResponse(status.HTTP_404_NOT_FOUND, "Review not found", "NOT_FOUND")
    return toilet.reviews


async def create_toilet_service(toilet: ToiletInDAO, user_id: PyObjectId):
    toilet.userId = user_id
    return await create_toilet(toilet)


async def update_toilet_service(
    toilet_id: PyObjectId, edit_toilet: ToiletInDAO, user_id: PyObjectId
):
    toilet = await get_toilet_by_id(toilet_id)
    if not toilet:
        raise ErrorResponse(status.HTTP_404_NOT_FOUND, "Toilet not found", "NOT_FOUND")
    if toilet.userId != user_id:
        raise ErrorResponse(
            status.HTTP_403_FORBIDDEN,
            "You are not allowed to edit this toilet",
            "FORBIDDEN",
        )
    return await update_toilet(toilet_id, edit_toilet)


async def delete_toilet_service(toilet_id: PyObjectId, user_id: PyObjectId):
    toilet = await get_toilet_by_id(toilet_id)
    if not toilet:
        raise ErrorResponse(status.HTTP_404_NOT_FOUND, "Toilet not found", "NOT_FOUND")
    if toilet.userId != user_id:
        raise ErrorResponse(
            status.HTTP_403_FORBIDDEN,
            "You are not allowed to delete this toilet",
            "FORBIDDEN",
        )
    return await delete_toilet(toilet_id)


async def create_toilet_review_service(
    toilet_id: PyObjectId, review: Review, user_id: PyObjectId
):
    toilet = await get_toilet_by_id(toilet_id)
    if not toilet:
        raise ErrorResponse(status.HTTP_404_NOT_FOUND, "Toilet not found", "NOT_FOUND")
    review.userId = user_id
    return await create_toilet_review(toilet_id, review)


async def update_toilet_review_service(
    toilet_id: PyObjectId, review: Review, user_id: PyObjectId
):
    toilet = await get_toilet_by_id(toilet_id)
    if not toilet:
        raise ErrorResponse(status.HTTP_404_NOT_FOUND, "Toilet not found", "NOT_FOUND")
    if toilet.userId != user_id:
        raise ErrorResponse(
            status.HTTP_403_FORBIDDEN,
            "You are not allowed to edit this review",
            "FORBIDDEN",
        )
    return await update_toilet_review(toilet_id, user_id, review)


async def delete_toilet_review_service(toilet_id: PyObjectId, user_id: PyObjectId):
    toilet = await get_toilet_by_id(toilet_id)
    if not toilet:
        raise ErrorResponse(status.HTTP_404_NOT_FOUND, "Toilet not found", "NOT_FOUND")
    if toilet.userId != user_id:
        raise ErrorResponse(
            status.HTTP_403_FORBIDDEN,
            "You are not allowed to delete this review",
            "FORBIDDEN",
        )
    return await delete_toilet_review(toilet_id, user_id)
