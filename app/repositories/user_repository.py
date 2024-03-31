from app.config.database import db
from app.models.mongo import PyObjectId
from app.models.user import UserInDAO, UserOutDAO


async def create_user(user: UserInDAO) -> UserOutDAO | None:
    response = await db.users.insert_one(user.mongo())
    return UserOutDAO.from_mongo(await db.users.find_one({"_id": response.inserted_id}))


async def update_user(user_id: PyObjectId, user: UserInDAO) -> UserOutDAO | None:
    response = await db.users.find_one_and_update(
        {"_id": user_id}, {"$set": user.mongo(exclude_none=True)}
    )
    return UserOutDAO.from_mongo(response)


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
