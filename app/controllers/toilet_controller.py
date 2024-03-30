from fastapi import APIRouter, Depends

from app.services.token_service import validate_token_service

toilet_controller = APIRouter(
    prefix="/toilets", tags=["toilets"], dependencies=[Depends(validate_token_service)]
)


@toilet_controller.get(
    "/",
    summary="Get all toilets",
    description="Get all toilets",
)
async def get_toilets():
    return "Get all toilets"
