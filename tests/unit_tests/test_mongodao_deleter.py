import pytest

from tests.constants import FAKE_COLLECTION, MONGO_TEST_DOCUMENT


class TestMongoDAODeleter:
    @pytest.mark.parametrize(
        "key,value", [(k, v) for k, v in MONGO_TEST_DOCUMENT.items()]
    )
    @pytest.mark.asyncio
    async def test_delete_one(self, deleter, temp_collection, key, value, writer):
        await writer.insert_one(temp_collection, {key: value})
        delete_op_result = await deleter.delete_one(
            temp_collection, filter_={key: value}
        )
        assert delete_op_result.deleted_count == 1

    @pytest.mark.parametrize(
        "key,value", [(k, v) for k, v in MONGO_TEST_DOCUMENT.items()]
    )
    @pytest.mark.asyncio
    async def test_delete_many(self, deleter, temp_collection, key, value, writer):
        await writer.insert_one(temp_collection, {key: value})
        delete_op_result = await deleter.delete_many(
            temp_collection, filter_={key: value}
        )
        assert delete_op_result.deleted_count == 1

    @pytest.mark.parametrize(
        "key,value", [(k, v) for k, v in MONGO_TEST_DOCUMENT.items()]
    )
    @pytest.mark.asyncio
    async def test_delete_one_no_match(self, deleter, temp_collection, key, value):
        delete_op_result = await deleter.delete_one(
            temp_collection, filter_={key: value}
        )
        assert delete_op_result.deleted_count == 0

    @pytest.mark.parametrize(
        "key,value", [(k, v) for k, v in MONGO_TEST_DOCUMENT.items()]
    )
    @pytest.mark.asyncio
    async def test_delete_many_no_match(self, deleter, temp_collection, key, value):
        delete_op_result = await deleter.delete_many(
            temp_collection, filter_={key: value}
        )
        assert delete_op_result.deleted_count == 0

    @pytest.mark.parametrize("fake_coll", [coll for coll in FAKE_COLLECTION])
    @pytest.mark.asyncio
    async def test_delete_one_wrong_fmt_error(self, deleter, fake_coll):
        with pytest.raises(Exception):
            await deleter.delete_one(fake_coll, filter_={})

    @pytest.mark.parametrize("fake_coll", [coll for coll in FAKE_COLLECTION])
    @pytest.mark.asyncio
    async def test_delete_many_wrong_fmt_error(self, deleter, fake_coll):
        with pytest.raises(Exception):
            await deleter.delete_many(fake_coll, filter_={})
