from motor.motor_asyncio import AsyncIOMotorClient

from database.dao import MongoDAOConnector
from settings.settings import settings


TEST_CLIENT_MONGO: AsyncIOMotorClient = MongoDAOConnector(
    host=settings.DATABASE_HOST_TEST,
    port=int(settings.DATABASE_PORT_TEST),
)
