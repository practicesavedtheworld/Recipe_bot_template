import abc

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase,
    AsyncIOMotorCollection,
)
from pymongo.results import UpdateResult

from settings.settings import settings


class BaseMongoDAOConnector(abc.ABC):
    """ Base abstract class for MongoDB DAO. """

    @abc.abstractmethod
    def __init__(self, host: str, port: int) -> None: ...

    @abc.abstractmethod
    def connect(self) -> AsyncIOMotorClient:
        """ Connect to MongoDB. """
        ...


class MongoDAOConnector(BaseMongoDAOConnector):
    """ Class for MongoDB DAO. """

    def __init__(self, host: str, port: int) -> None:
        self._host = host
        self._port = port

    def connect(self) -> AsyncIOMotorClient:
        return AsyncIOMotorClient(self._host, self._port)


###############################
##          READER           ##
###############################
class MongoDAOReader:
    """ Interface reader for MongoDB DAO. """

    @staticmethod
    async def find_one(
            aio_collection: AsyncIOMotorCollection,
            filter_: dict | None = None,
    ) -> dict | None:
        """ Find one document. """

        document = await aio_collection.find_one(filter=filter_)
        return document

    @staticmethod
    async def find_many(
            aio_collection: AsyncIOMotorCollection,
            filter_: dict | None = None
    ) -> list[dict]:
        """ Find many documents. """

        cursor = aio_collection.find(filter=filter_)
        res = []
        async for doc in cursor:
            res.append(doc)
        return res


###############################
##          WRITER           ##
###############################
class MongoDAOWriter:
    """ Interface writer for MongoDB DAO. """

    @staticmethod
    async def insert_one(
            aio_collection: AsyncIOMotorCollection,
            document: dict,
    ) -> None:
        """ Insert one document. """

        await aio_collection.insert_one(document)

    @staticmethod
    async def insert_many(
            aio_collection: AsyncIOMotorCollection,
            documents: list[dict],
    ) -> None:
        """ Insert many documents. """

        await aio_collection.insert_many(documents)


###############################
##         UPDATER           ##
###############################
class MongoDAOUpdater:
    """ Interface updater for MongoDB DAO. """

    @staticmethod
    async def update_one(
            aio_collection: AsyncIOMotorCollection,
            filter_: dict,
            update: dict,
    ) -> UpdateResult:
        """ Update first found one document. """

        return await aio_collection.update_one(filter=filter_, update=update)

    @staticmethod
    async def update_many(
            aio_collection: AsyncIOMotorCollection,
            filter_: dict,
            update: dict,
    ) -> UpdateResult:
        """ Update many documents. """

        return await aio_collection.update_many(filter=filter_, update=update)


###############################
##          DELETER          ##
###############################
class MongoDAODeleter:
    """ Interface deleter for MongoDB DAO. """

    @staticmethod
    async def delete_one(
            aio_collection: AsyncIOMotorCollection,
            filter_: dict,
    ) -> None:
        """ Immediately removes the first returned matching document."""

        await aio_collection.delete_one(filter_)

    @staticmethod
    async def delete_many(
            aio_collection: AsyncIOMotorCollection,
            filter_: dict,
    ) -> None:
        """ Delete multiple documents. Immediately removes all matching documents."""

        await aio_collection.delete_many(filter_)


try:
    client: AsyncIOMotorClient = MongoDAOConnector(
        host=settings.DATABASE_HOST,
        port=int(settings.DATABASE_PORT),
    ).connect()
    db: AsyncIOMotorDatabase = client.test1
    db_reader, db_writer, db_updater, db_deleter = (
        MongoDAOReader(),
        MongoDAOWriter(),
        MongoDAOUpdater(),
        MongoDAODeleter(),
    )
    recipes_collection = db["recipes"]

except:
    # TODO exception
    print("MongoDB not available. Skipping tests.")
