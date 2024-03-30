from app.config.database import db
from app.models.authentification import TokenInDAO, TokenOutDAO


async def create_token(token: TokenInDAO) -> TokenOutDAO | None:
    response = await db.tokens.insert_one(token.mongo())
    return TokenOutDAO.from_mongo(
        await db.tokens.find_one({"_id": response.inserted_id})
    )


async def get_token(user_id: str) -> TokenOutDAO | None:
    token = await db.tokens.find_one({"user_id": user_id})
    if token:
        return TokenOutDAO.from_mongo(token)
    return None
