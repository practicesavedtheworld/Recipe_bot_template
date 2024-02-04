import abc
from dataclasses import dataclass
from typing import Optional

from recipes.ingredient import Ingredient


class RecipeAbc(abc.ABC):
    """Base abstract class for recipes."""

    @abc.abstractmethod
    def __contains__(self, item: Ingredient) -> bool: ...

    @abc.abstractmethod
    def __repr__(self) -> str: ...


@dataclass
class Recipe(RecipeAbc):
    """Class that represents a recipe."""

    _recipe_name: str
    _ingredients: list[tuple[Ingredient, Optional[str]]]
    _cooking_method: str

    def __post_init__(self):
        self._recipe_name = self._recipe_name.capitalize()

    @property
    def recipe_name(self):
        return self._recipe_name

    @property
    def ingredients(self):
        return self._ingredients

    @property
    def cooking_method(self):
        return self._cooking_method

    def __repr__(self) -> str:
        ingredients = "\n".join(
            [f"{ingr[0]} - {ingr[1]}" for ingr in self._ingredients]
        )
        return f"{self._recipe_name}:\n{ingredients}\n{self._cooking_method}"

    def __str__(self) -> str:
        return self.__repr__()

    def __contains__(self, item: Ingredient) -> bool:
        if isinstance(item, Ingredient):
            return item in self._ingredients
        return False

