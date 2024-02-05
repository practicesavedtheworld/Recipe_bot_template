from typing import Any

from database.dao import MongoDAOConnector
from settings.settings import settings

MONGO_TEST_DOCUMENT: dict[str, str] = {
    "k1": "v1",
    "k2": "v2",
    "k3": "v3",
    "k4": "v4",
    "k5": "v5",
}
FAKE_COLLECTION: tuple[Any, ...] = (
    [],
    None,
    {},
)
TEST_CLIENT_MONGO: MongoDAOConnector = MongoDAOConnector(
    host=settings.DATABASE_HOST_TEST,
    port=int(settings.DATABASE_PORT_TEST),
)
