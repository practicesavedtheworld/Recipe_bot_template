from pytest import fixture

from database.dao import (
    db_reader,
    db_writer,
    db_updater,
    db_deleter,
    client
)


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
    test_db = client.testdb
    coll = test_db["test"]

    yield coll

    # client.drop_database(test_db)
