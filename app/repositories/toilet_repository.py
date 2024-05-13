from app.config.database import db
from app.models.mongo import PyObjectId
from app.models.toilet import Review, ReviewOutDAO, ToiletInDAO, ToiletOutDAO


async def create_toilet(toilet: ToiletInDAO) -> ToiletOutDAO | None:
    response = await db.toilets.find_one_and_update(
        {"_id": PyObjectId()},
        {"$set": toilet.dict()},
        upsert=True,
        return_document=True,
    )
    return ToiletOutDAO.from_mongo(response)


async def update_toilet(
    toilet_id: PyObjectId, toilet: ToiletInDAO
) -> ToiletOutDAO | None:
    response = await db.toilets.find_one_and_update(
        {"_id": toilet_id},
        {"$set": toilet.dict(exclude_none=True)},
        upsert=False,
        return_document=True,
    )
    return ToiletOutDAO.from_mongo(response)


async def get_toilet_by_id(toilet_id: PyObjectId) -> ToiletOutDAO | None:
    toilet = await db.toilets.find_one({"_id": toilet_id})
    if toilet:
        return ToiletOutDAO.from_mongo(toilet)
    return None


async def get_toilets_details() -> list[ToiletOutDAO]:
    response = await db.toilets.find().to_list(None)
    return ToiletOutDAO.from_mongo_list(response)


async def get_toilets_by_user(user_id: PyObjectId) -> list[ToiletOutDAO]:
    response = await db.toilets.find({"userId": user_id}).to_list(None)
    return ToiletOutDAO.from_mongo_list(response)


async def delete_toilet(toilet_id: PyObjectId) -> bool:
    return bool(await db.toilets.delete_one({"_id": toilet_id}))


async def get_toilet_reviews(toilet_id: PyObjectId) -> list[ReviewOutDAO]:
    response = await db.review.find({"toiletId": toilet_id}).to_list(None)
    return ReviewOutDAO.from_mongo_list(response)


async def create_toilet_review(
    toilet_id: PyObjectId, review: Review
) -> ToiletOutDAO | None:
    response = await db.toilets.find_one_and_update(
        {"_id": toilet_id}, {"$push": {"reviews": review.dict()}}
    )
    return ToiletOutDAO.from_mongo(response)


async def update_toilet_review(
    toilet_id: PyObjectId, user_id: PyObjectId, review: Review
) -> ToiletOutDAO | None:
    response = await db.toilets.find_one_and_update(
        {"_id": toilet_id, "reviews.userId": user_id},
        {"$set": {"reviews.$": review.dict()}},
    )
    return ToiletOutDAO.from_mongo(response)


async def delete_toilet_review(
    toilet_id: PyObjectId, user_id: PyObjectId
) -> ToiletOutDAO | None:
    response = await db.toilets.find_one_and_update(
        {"_id": toilet_id},
        {"$pull": {"reviews": {"userId": user_id}}},
    )
    return ToiletOutDAO.from_mongo(response)
