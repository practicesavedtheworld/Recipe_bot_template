from database.schemas import FoundRecipeScheme


def human_readable_recipe(recipe: FoundRecipeScheme) -> str:
    """Converts a recipe dict into a human-readable string."""

    name, ingredients, method = (recipe.recipe_name, recipe.ingredients, recipe.method)
    return f"{name}\n\n{ingredients}\n\n{method}"
