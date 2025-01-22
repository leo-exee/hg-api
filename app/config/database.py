import logging
from datetime import timezone

import motor.motor_asyncio
from bson import CodecOptions

from app.config.constants import MONGODB_URL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

db = client.hg.with_options(
    codec_options=CodecOptions(tz_aware=True, tzinfo=timezone.utc)
)


async def connect_to_mongo():
    logger.info("Connecting to database...")
    global client
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)


async def close_mongo_connection():
    logger.info("Closing connection to database...")
    client.close()
