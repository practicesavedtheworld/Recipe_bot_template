from pytest import fixture

from database.dao import db_deleter, db_reader, db_updater, db_writer
from tests.constants import TEST_CLIENT_MONGO


@fixture()
def reader():
    return db_reader


@fixture()
def writer():
    return db_writer


@fixture()
def updater():
    return db_updater


@fixture()
def deleter():
    return db_deleter


@fixture(scope="function")
def temp_collection():
    """Create temporary MongoDB collection."""

    test_db = TEST_CLIENT_MONGO.connect().testdb
    coll = test_db["test"]

    yield coll

    TEST_CLIENT_MONGO.connect().drop_database(test_db)
