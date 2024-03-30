from app.config.database import db
from app.models.authentification import TokenInDAO, TokenOutDAO
from app.models.mongo import PyObjectId


async def create_token(token: TokenInDAO) -> TokenOutDAO | None:
    response = await db.tokens.insert_one(token.mongo())
    return TokenOutDAO.from_mongo(
        await db.tokens.find_one({"_id": response.inserted_id})
    )


async def get_token(token: str) -> TokenOutDAO | None:
    response = await db.tokens.find_one({"token": token})
    if response:
        return TokenOutDAO.from_mongo(response)
    return None


async def get_token_by_user_id(user_id: PyObjectId) -> TokenOutDAO | None:
    response = await db.tokens.find_one({"userId": user_id})
    if response:
        return TokenOutDAO.from_mongo(response)
    return None
