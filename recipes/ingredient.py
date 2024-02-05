import abc
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class IngredientAbc(ABC):
    """Base abstract class for ingredients."""

    def __str__(self) -> str:
        return self.__repr__()

    @abc.abstractmethod
    def __repr__(self) -> str: ...

    @abc.abstractmethod
    def __eq__(self, other) -> bool: ...

    @property
    @abc.abstractmethod
    def useful_properties(self) -> dict[int, str]: ...

    @abc.abstractmethod
    def __contains__(self, item: str) -> bool: ...


@dataclass
class Ingredient(IngredientAbc):
    """Class that represents an ingredient."""

    _ingredient_name: str
    _calories: float = field(default=0.0)

    def __post_init__(self) -> None:
        self._ingredient_name = self._ingredient_name.capitalize()
        self._useful_properties: dict[int, str] = {}

    def __contains__(self, item):
        return item in self._useful_properties.values()

    def __repr__(self) -> str:
        return self._ingredient_name

    def __hash__(self) -> int:
        return hash(self._ingredient_name)

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, Ingredient)
            and other._ingredient_name.lower().strip()
            == self._ingredient_name.lower().strip()
        )

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        if hasattr(self, "_calories"):
            self._calories = value

    @property
    def name(self):
        return self._ingredient_name

    @property
    def useful_properties(self) -> dict[int, str]:
        """Returns a dictionary of useful properties for the ingredient."""

        return self._useful_properties


def is_ingredient(obj) -> bool:
    return isinstance(obj, Ingredient)


class IngredientModifier:
    """Modifies ingredients."""

    @staticmethod
    def add_property(ingredient: Ingredient, prop: str) -> None:
        """Adds a property to the ingredient."""

        if (
            is_ingredient(ingredient)
            and isinstance(prop, str)
            and prop not in ingredient
        ):
            ingredient.useful_properties[len(ingredient.useful_properties) + 1] = prop

    @staticmethod
    def remove_property(ingredient: Ingredient, prop: str) -> None:
        """Removes a property from the ingredient."""

        if is_ingredient(ingredient) and isinstance(prop, str) and prop in ingredient:
            for k, v in ingredient.useful_properties.items():
                if v == prop:
                    del ingredient.useful_properties[k]
                    break

    @staticmethod
    def set_ingredient_calories(ingredient: Ingredient, calories: int) -> None:
        """Sets the calories of the ingredient."""

        if is_ingredient(ingredient) and isinstance(calories, int):
            ingredient.calories = calories


class IngredientsStorageAbc(ABC):
    """Base abstract class for ingredients storage."""

    _ingredient_id_map: dict[Ingredient, int] = {}

    @property
    def ingredient_id_map(self):
        return self._ingredient_id_map

    @abc.abstractmethod
    def __contains__(self, ingredient: Ingredient) -> bool: ...

    @abc.abstractmethod
    def __repr__(self) -> str: ...


class IngredientsStorage(IngredientsStorageAbc):
    """Stores all the ingredients."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __repr__(self) -> str:
        return str(self._ingredient_id_map.keys())

    def __contains__(self, ingredient: Ingredient) -> bool:
        """Checks if the ingredient is present in the ingredient ID map."""

        if is_ingredient(ingredient):
            return ingredient in self._ingredient_id_map
        return False


class IngredientStorageModifier:
    """Modifies ingredients."""

    @staticmethod
    def add_ingredient(ingredient: Ingredient, storage: IngredientsStorageAbc) -> None:
        """Adds an ingredient to the ingredient ID map."""

        if is_ingredient(ingredient) and ingredient not in storage:
            storage.ingredient_id_map[ingredient] = len(storage.ingredient_id_map) + 1

    @staticmethod
    def remove_ingredient(
        ingredient: Ingredient, storage: IngredientsStorageAbc
    ) -> None:
        """Removes an ingredient from the ingredient ID map."""

        if is_ingredient(ingredient) and ingredient in storage:
            del storage.ingredient_id_map[ingredient]


class IngredientStorageSearcher:
    """Searches ingredients."""

    @staticmethod
    def get_iid_by_ingredient(
        ingredient: Ingredient, i_storage: IngredientsStorageAbc
    ) -> int | None:
        """Returns the ID of an ingredient from the ingredient ID map."""

        if is_ingredient(ingredient):
            return i_storage.ingredient_id_map.get(ingredient)

    @staticmethod
    def get_ingredient_by_iid(
        iid: int, i_storage: IngredientsStorageAbc
    ) -> Ingredient | None:
        """Returns an ingredient from the ingredient ID map."""

        if iid in i_storage.ingredient_id_map.values():
            return list(i_storage.ingredient_id_map.keys())[iid - 1]


################################################
#               Coming soon section            #
#      It flexible, so you can extend logic    #
################################################
class IngredientGroupAbc(ABC):
    """Base abstract class for ingredient groups."""

    @abstractmethod
    def __repr__(self) -> str:
        pass


@dataclass
class IngredientGroup(IngredientGroupAbc):
    """Represents an ingredient group."""

    _group_name: str = "Ingredient Group"
    _ingredients: set[Ingredient] = field(default_factory=set)

    def __contains__(self, ingredient: Ingredient) -> bool:
        return ingredient in self._ingredients

    def __repr__(self) -> str:
        return f"{self._group_name}: {self._ingredients}"

    @property
    def ingredients(self):
        return self._ingredients


class IngredientGroupModifier:
    """Modifies ingredient groups."""

    @staticmethod
    def add_ingredient(group: IngredientGroup, ingredient: Ingredient) -> None:
        """Adds an ingredient to the ingredient group."""

        if isinstance(ingredient, Ingredient):
            group.ingredients.add(ingredient)

    @staticmethod
    def remove_ingredient(group: IngredientGroup, ingredient: Ingredient) -> None:
        """Removes an ingredient from the ingredient group."""

        if ingredient in group.ingredients:
            group.ingredients.remove(ingredient)


class IngredientGroupSortInterface(ABC):
    """Interface for sorting ingredient groups."""

    @abstractmethod
    def sort_ingredients(self, group: IngredientGroup):
        pass


class IngredientGroupNameSorter(IngredientGroupSortInterface):
    """Sorts ingredient groups by name."""

    def sort_ingredients(self, group: IngredientGroup) -> list[Ingredient]:
        """Ascending order."""

        return sorted(group.ingredients, key=lambda x: x.name)


# @dataclass
# class Meat(IngredientGroup):
#     """Represents a meat ingredient group."""
#
#     _group_name: str = "Meat"
#     _ingredients: set[Ingredient] = field(default_factory=set)
