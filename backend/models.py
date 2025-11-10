from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class UserMood(BaseModel):
    mood_description: str
    timestamp: datetime

class Recipe(BaseModel):
    recipe_id: int
    name: str
    ingredients: List[str]
    instructions: str
    mood_tags: List[str]

class User(BaseModel):
    user_id: int
    username: str
    hashed_password: str
    email: str

class Favorite(BaseModel):
    user_id: int
    recipe_id: int

class RatingFeedback(BaseModel):
    user_id: int
    recipe_id: int
    rating: int  # 1-5
    comment: Optional[str] = None
