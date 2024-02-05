import pytest

from tests.constants import MONGO_TEST_DOCUMENT


class TestMongoDAOWriter:

    @pytest.mark.asyncio
    async def test_insert_one_empty(self, writer, temp_collection, reader):
        await writer.insert_one(temp_collection, {})
        assert len(await reader.find_many(temp_collection, {})) == 1

    @pytest.mark.asyncio
    async def test_insert_many_empty(self, writer, temp_collection, reader):
        await writer.insert_many(temp_collection, [{}])
        assert len(await reader.find_many(temp_collection, {})) == 1

    @pytest.mark.parametrize(
        "document",
        [
            None,
            ([[{"recipe_name": "test"}]]),
        ],
    )
    @pytest.mark.asyncio
    async def test_insert_wrong_fmt_error(self, writer, temp_collection, document):
        with pytest.raises(Exception):
            await writer.insert_one(temp_collection, document=document)

    @pytest.mark.parametrize(
        "key,value", [(k, v) for k, v in MONGO_TEST_DOCUMENT.items()]
    )
    @pytest.mark.asyncio
    async def test_insert_many(self, writer, temp_collection, reader, key, value):
        await writer.insert_many(temp_collection, [{key: value}])
        assert len(await reader.find_many(temp_collection, {key: value})) == 1

    @pytest.mark.parametrize(
        "key,value", [(k, v) for k, v in MONGO_TEST_DOCUMENT.items()]
    )
    @pytest.mark.asyncio
    async def test_insert_one(self, writer, temp_collection, reader, key, value):
        await writer.insert_one(temp_collection, {key: value})
        assert len(await reader.find_many(temp_collection, {key: value})) == 1
