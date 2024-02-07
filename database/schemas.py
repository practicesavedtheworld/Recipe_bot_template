from bson import ObjectId
from pydantic import BaseModel


class FoundRecipeScheme(BaseModel):
    _id: ObjectId
    recipe_name: str
    ingredients: str
    method: str
