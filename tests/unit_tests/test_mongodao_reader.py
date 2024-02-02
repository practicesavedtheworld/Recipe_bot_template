import pytest


class TestMongoDAOReader:

    @pytest.mark.asyncio
    async def test_find_one_on_empty_collection(self, reader, temp_collection):
        find_res = await reader.find_one(temp_collection, filter_={})
        assert find_res is None

    @pytest.mark.asyncio
    async def test_find_many_on_empty_collection(self, reader, temp_collection):
        find_res = await reader.find_many(temp_collection, filter_={})
        assert len(find_res) == 0

    @pytest.mark.parametrize(
        "filter_,expected",
        [
            ({"recipe_name": "test"}, "test"),
            ({"recipe_name": {"d": "d"}}, {"d": "d"}),
            ({"recipe_name": "another_test"}, "another_test"),
            ({"recipe_name": {"a": None}}, {"a": None}),
        ],
    )
    @pytest.mark.asyncio
    async def test_find_one(self, reader, temp_collection, filter_, expected):
        await temp_collection.insert_one(filter_)
        find_res = await reader.find_one(temp_collection, filter_)
        assert find_res is not None
        assert find_res["recipe_name"] == expected

    @pytest.mark.parametrize(
        "filter_",
        [
            ({"recipe_name": "test"}),
            ({"recipe_name": {"d": "d"}}),
            ({"recipe_name": "another_test"}),
            ({"recipe_name": {"a": None}}),
        ],
    )
    @pytest.mark.asyncio
    async def test_find_many(self, reader, temp_collection, filter_):
        await temp_collection.insert_one(filter_)
        find_res = await reader.find_many(temp_collection, filter_)
        assert len(find_res) == 1
        assert find_res[0]["recipe_name"] == filter_["recipe_name"]
