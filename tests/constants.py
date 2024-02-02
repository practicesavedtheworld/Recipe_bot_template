from motor.motor_asyncio import AsyncIOMotorClient

from database.dao import MongoDAOConnector
from settings.settings import settings

MONGO_TEST_DOCUMENT = {
    "k1": "v1",
    "k2": "v2",
    "k3": "v3",
    "k4": "v4",
    "k5": "v5",
}
FAKE_COLLECTION = (
    [],
    None,
    {},
)
TEST_CLIENT_MONGO: AsyncIOMotorClient = MongoDAOConnector(
    host=settings.DATABASE_HOST_TEST,
    port=int(settings.DATABASE_PORT_TEST),
)
