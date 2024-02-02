import pytest

from tests.constants import MONGO_TEST_DOCUMENT


class TestMongoDAOUpdater:
    @pytest.mark.parametrize(
        "key,value", [(k, v) for k, v in MONGO_TEST_DOCUMENT.items()]
    )
    @pytest.mark.asyncio
    async def test_update_one(self, updater, temp_collection, key, value, writer):
        await writer.insert_one(temp_collection, {key: value})
        update_op_result = await updater.update_one(
            temp_collection,
            filter_={key: value},
            update={"$set": {"test": "test"}},
        )
        assert (
            update_op_result.matched_count == 1 and update_op_result.modified_count == 1
        )

    @pytest.mark.parametrize(
        "key,value", [(k, v) for k, v in MONGO_TEST_DOCUMENT.items()]
    )
    @pytest.mark.asyncio
    async def test_update_many(self, updater, temp_collection, key, value, writer):
        await writer.insert_one(temp_collection, {key: value})
        update_op_result = await updater.update_many(
            temp_collection,
            filter_={key: value},
            update={"$set": {"test": "test"}},
        )
        assert (
            update_op_result.matched_count == 1 and update_op_result.modified_count == 1
        )

    @pytest.mark.parametrize(
        "key,value", [(k, v) for k, v in MONGO_TEST_DOCUMENT.items()]
    )
    @pytest.mark.asyncio
    async def test_update_one_wrong_fmt_error(
        self, updater, temp_collection, key, value
    ):
        with pytest.raises(Exception):
            await updater.update_one(
                temp_collection,
                filter_={key: value},
                update={{"test": "test"}},
            )

    @pytest.mark.parametrize(
        "key,value", [(k, v) for k, v in MONGO_TEST_DOCUMENT.items()]
    )
    @pytest.mark.asyncio
    async def test_update_many_wrong_fmt_error(
        self, updater, temp_collection, key, value
    ):
        with pytest.raises(Exception):
            await updater.update_many(
                temp_collection,
                filter_={key: value},
                update={{"test": "test"}},
            )

    @pytest.mark.asyncio
    async def test_update_one_no_match(self, updater, temp_collection):
        update_op_result = await updater.update_one(
            temp_collection, filter_={}, update={"$set": {"test": "test"}}
        )
        assert (
            update_op_result.matched_count == 0 and update_op_result.modified_count == 0
        )

    @pytest.mark.asyncio
    async def test_update_many_no_match(self, updater, temp_collection):
        update_op_result = await updater.update_many(
            temp_collection, filter_={}, update={"$set": {"test": "test"}}
        )
        assert (
            update_op_result.matched_count == 0 and update_op_result.modified_count == 0
        )
