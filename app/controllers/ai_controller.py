from fastapi import APIRouter, Depends

from app.models.toilet import Content
from app.services.ai_service import generate_description_service
from app.services.token_service import get_token_user_service

ai_controller = APIRouter(
    prefix="/ai", tags=["ai"], dependencies=[Depends(get_token_user_service)]
)


@ai_controller.post("/describe")
async def describe(content: Content):
    return await generate_description_service(content)
