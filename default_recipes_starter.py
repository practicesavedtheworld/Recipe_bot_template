#!usr/bin/env python3

import asyncio

from database.dao import db_writer, recipes_collection
from recipes.ingredient import Ingredient, IngredientsStorage, IngredientStorageModifier
from recipes.recipe import Recipe
from utils.datasets import get_recipes_from_txt


def push_ingredients_to_storage(
    ingredient: Ingredient, storage: IngredientsStorage
) -> str:
    """Pushes ingredients to storage. Returns ingredient name.
    If this is a new ingredient, it will be added to the storage.
    If ingredient in db it also will be added to the storage.
    """

    IngredientStorageModifier().add_ingredient(ingredient, storage)
    return ingredient.name


async def push_default_recipes() -> None:
    """ Pushes default recipes to the database."""

    rcs: list[Recipe] = get_recipes_from_txt()
    await db_writer.insert_many(
        recipes_collection,
        [
            {
                "recipe_name": r.recipe_name,
                "ingredients": "\n".join(
                    [
                        f"{push_ingredients_to_storage(
                            ingr[0],
                            IngredientsStorage(),
                        )} - "
                        f"{ingr[1]}"
                        for ingr in r.ingredients
                    ]
                ),
                "method": r.cooking_method,
            }
            for r in rcs
        ],
    )


if __name__ == "__main__":

    async def main():
        await push_default_recipes()

    asyncio.run(main())
