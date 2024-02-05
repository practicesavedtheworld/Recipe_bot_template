import csv
from typing import Optional

from recipes.ingredient import Ingredient
from recipes.recipe import Recipe
from utils.constants import PROJECT_ROOT


def find_ingredient_calory_value_from_csv(ingredient_name) -> float | None:
    """Looking for ingredient calories in csv file.
    CSV file has format: name,unit,CCal"""

    with open(
        f"{PROJECT_ROOT}/default_datasets/ingredients.csv", "r", encoding="UTF-8"
    ) as f:
        reader = csv.reader(f)
        for row in reader:
            if ingredient_name.lower() == row[0].lower():
                return float(row[-1])


def get_recipes_from_txt() -> list[Recipe]:
    """Generates RU recipes from recipes.txt file"""

    with open(
        f"{PROJECT_ROOT}/default_datasets/recipes.txt", "r", encoding="UTF-8"
    ) as recipes_txt:
        rec = recipes_txt.read().split("---------------------------")
        found_recipes = []
        for curr_rec in rec:
            dish = curr_rec.split("\n\n")
            name, ingredients, method = dish[0], dish[1], dish[2]

            for idx, el in enumerate([name, ingredients, method]):
                el = el.split("\n")[1:]  # type: ignore
                full_elem = "\n".join(
                    [elem.strip() for elem in el if not elem.startswith("Наз")]
                )
                match idx:
                    case 0:
                        recipe_name = full_elem
                    case 1:
                        ingredients_list: list[tuple[Ingredient, Optional[str]]] = []
                        for ingr in full_elem.split("\n"):
                            ingredient_name, ingredient_quantity = ingr.split(" - ")
                            cal = find_ingredient_calory_value_from_csv(ingredient_name)
                            ingredients_list.append(
                                (
                                    Ingredient(
                                        _ingredient_name=ingredient_name,
                                        _calories=cal if cal else 0.0,
                                    ),
                                    ingredient_quantity,
                                )
                            )

                    case 2:
                        recipe_method = full_elem
            found_recipes.append(
                Recipe(
                    _recipe_name=recipe_name,
                    _ingredients=ingredients_list,
                    _cooking_method=recipe_method,
                )
            )
        return found_recipes
