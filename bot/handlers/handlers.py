from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import hbold
from bson import ObjectId

from bot.loader import bot
from database.dao import db_reader, recipes_collection
from database.schemas import FoundRecipeScheme
from utils.constants import DEFAULT_RECIPE_IMAGE_PATH
from utils.recipe import human_readable_recipe

router = Router()


@router.message(Command("recipes"))
async def recipes(message: types.Message):
    """Shows all recipes available."""
    recipe_kb = InlineKeyboardBuilder()

    rec = await db_reader.find_many(aio_collection=recipes_collection)
    for r in rec:
        rec_id = str(r["_id"])
        recipe_kb.row(
            types.InlineKeyboardButton(
                text=r["recipe_name"], callback_data=f"found_recipe:{rec_id}"
            )
        )

    await message.answer_photo(
        types.FSInputFile(path=DEFAULT_RECIPE_IMAGE_PATH),
        caption="Choose recipe",
        reply_markup=recipe_kb.as_markup(),
    )


@router.callback_query(lambda c: c.data.startswith("found_recipe:"))
async def found_recipe(query: types.CallbackQuery):
    recipe_id = query.data[query.data.find(":") + 1 :]  # type: ignore
    rec = await db_reader.find_one(
        aio_collection=recipes_collection, filter_={"_id": ObjectId(recipe_id)}
    )
    if rec:
        await bot.send_message(
            chat_id=query.from_user.id,
            text=human_readable_recipe(FoundRecipeScheme(**rec)),
        )
    else:
        await bot.send_message(chat_id=query.from_user.id, text="Recipe not found.")


@router.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    """Greeting message when user starts bot."""

    await message.answer(
        hbold(
            f"hi {message.from_user.full_name}. "  # type: ignore
            f"Type /recipes to see available recipes."
        )
    )


################################################
#               Coming soon section            #
################################################
@router.message(Command("Add"))
async def add_recipe(message: types.Message) -> None:
    """Sending recipe for verification and if it is correct,
    it will be added to database.
    Recipe format:
    recipe name
    ingredients for recipe
    cooking method
    """

    await bot.send_message(
        chat_id=message.from_user.id,  # type: ignore
        text="This feature is coming soon. Check back later.",
    )
    pass
