"""
Main backend app for MVP
Handles REST API endpoints for moods, recipes, health check
Includes mood to recipe matching logic
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Mood Recipe MVP Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Data models
class UserMood(BaseModel):
    mood_description: str
    timestamp: datetime

class Recipe(BaseModel):
    recipe_id: int
    name: str
    ingredients: List[str]
    instructions: str
    mood_tags: List[str]

# In-memory example data
recipes_db = [
    Recipe(recipe_id=1, name="Chocolate Cake", ingredients=["flour", "sugar", "cocoa"], instructions="Bake it", mood_tags=["happy", "celebration"]),
    Recipe(recipe_id=2, name="Tomato Soup", ingredients=["tomato", "salt", "water"], instructions="Boil it", mood_tags=["sad", "comfort"])
]

@app.get("/api/mood", tags=["Moods"])
def get_moods():
    return {"message": "Use POST to submit mood data."}

@app.post("/api/mood", tags=["Moods"])
def post_mood(user_mood: UserMood):
    recommended = [recipe for recipe in recipes_db if user_mood.mood_description.lower() in recipe.mood_tags]
    if not recommended:
        raise HTTPException(status_code=404, detail="No recipes found for the mood")
    return {"recommended_recipes": recommended}

@app.get("/api/recipes/{recipe_id}", tags=["Recipes"])
def get_recipe(recipe_id: int):
    for recipe in recipes_db:
        if recipe.recipe_id == recipe_id:
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")

@app.get("/api/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
