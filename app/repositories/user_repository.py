from app.config.database import db
from app.models.mongo import PyObjectId
from app.models.user import UserInDAO, UserOutDAO


async def create_user(user: UserInDAO) -> UserOutDAO | None:
    response = await db.users.insert_one(user.mongo())
    new_user = await db.users.find_one({"_id": response.inserted_id})
    if not new_user:
        return None
    return UserOutDAO.from_mongo(new_user)


async def get_user(user_id: PyObjectId) -> UserOutDAO | None:
    user = await db.users.find_one({"_id": user_id})
    if user:
        return UserOutDAO.from_mongo(user)
    return None


async def get_user_by_auth(email: str) -> UserOutDAO | None:
    user = await db.users.find_one({"email": email})
    if user:
        return UserOutDAO.from_mongo(user)
    return None
