from __future__ import annotations

import abc
import logging
import pathlib
from typing import TYPE_CHECKING

from bot.exceptions.database_exceptions import DatabaseIsNotActiveException
from bot.exceptions.unexpected_exceptions import (
    StoppedByUserSignalException,
    UnexpectedException,
)

if TYPE_CHECKING:
    from motor.core import AgnosticClient, AgnosticDatabase, AgnosticCollection

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import BulkWriteError, ConnectionFailure
from pymongo.results import DeleteResult, UpdateResult

from settings.settings import settings
from utils.logger import create_logger

dao_loger = create_logger(
    loger_name="dao logger",
    logger_level=logging.DEBUG,
    file_info=pathlib.Path(__file__).name,
)


class BaseMongoDAOConnector(abc.ABC):
    """Base abstract class for MongoDB DAO."""

    @abc.abstractmethod
    def __init__(self, host: str, port: int) -> None: ...

    @abc.abstractmethod
    def connect(self) -> AgnosticClient:
        """Connect to MongoDB."""
        ...


class MongoDAOConnector(BaseMongoDAOConnector):
    """Class for MongoDB DAO."""

    def __init__(self, host: str, port: int) -> None:
        self._host = host
        self._port = port

    def connect(self) -> AgnosticClient:
        return AsyncIOMotorClient(self._host, self._port)


###############################
##          READER           ##
###############################
class MongoDAOReader:
    """Interface reader for MongoDB DAO."""

    @staticmethod
    async def find_one(
        aio_collection: AgnosticCollection,
        filter_: dict | None = None,
    ) -> dict | None:
        """Find one document."""

        document = await aio_collection.find_one(filter=filter_)
        return document

    @staticmethod
    async def find_many(
        aio_collection: AgnosticCollection,
        filter_: dict | None = None,
    ) -> list[dict]:
        """Find many documents."""

        cursor = aio_collection.find(filter=filter_)
        res = []
        async for doc in cursor:
            res.append(doc)
        return res


###############################
##          WRITER           ##
###############################
class MongoDAOWriter:
    """Interface writer for MongoDB DAO."""

    @staticmethod
    async def insert_one(
        aio_collection: AgnosticCollection,
        document: dict,
    ) -> None:
        """Insert one document."""

        await aio_collection.insert_one(document)

    @staticmethod
    async def insert_many(
        aio_collection: AgnosticCollection,
        documents: list[dict],
    ) -> None:
        """Insert many documents."""

        await aio_collection.insert_many(documents)


###############################
##         UPDATER           ##
###############################
class MongoDAOUpdater:
    """Interface updater for MongoDB DAO."""

    @staticmethod
    async def update_one(
        aio_collection: AgnosticCollection,
        filter_: dict,
        update: dict,
    ) -> UpdateResult:
        """Update first found one document."""

        return await aio_collection.update_one(filter=filter_, update=update)

    @staticmethod
    async def update_many(
        aio_collection: AgnosticCollection,
        filter_: dict,
        update: dict,
    ) -> UpdateResult:
        """Update many documents."""

        return await aio_collection.update_many(filter=filter_, update=update)


###############################
##          DELETER          ##
###############################
class MongoDAODeleter:
    """Interface deleter for MongoDB DAO."""

    @staticmethod
    async def delete_one(
        aio_collection: AgnosticCollection,
        filter_: dict,
    ) -> DeleteResult:
        """Immediately removes the first returned matching document."""

        return await aio_collection.delete_one(filter_)

    @staticmethod
    async def delete_many(
        aio_collection: AgnosticCollection,
        filter_: dict,
    ) -> DeleteResult:
        """Delete multiple documents. Immediately removes all matching documents."""

        return await aio_collection.delete_many(filter_)


try:
    client: AgnosticClient = MongoDAOConnector(
        host=settings.DATABASE_HOST,
        port=int(settings.DATABASE_PORT),
    ).connect()
    db: AgnosticDatabase = client.test1
    db_reader, db_writer, db_updater, db_deleter = (
        MongoDAOReader(),
        MongoDAOWriter(),
        MongoDAOUpdater(),
        MongoDAODeleter(),
    )
    recipes_collection = db["recipes"]

except (ConnectionFailure, BulkWriteError) as db_connection_err:
    dao_loger.debug("MongoDB not available. Skipping tests.")
    raise DatabaseIsNotActiveException(exc_details=db_connection_err.__repr__())
except KeyboardInterrupt as signal_err:
    raise StoppedByUserSignalException(exc_details=signal_err.__repr__())
except Exception as unexpected_error:
    raise UnexpectedException(exc_details=unexpected_error.__repr__())
