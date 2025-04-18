from pydantic import BaseModel

class RecipeBase(BaseModel):
    title: str
    ingredients: str
    instructions: str
    cooking_time: int
    servings: int
    image_url: str | None = None

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True