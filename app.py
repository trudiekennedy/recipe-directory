from lib.database_connection import DatabaseConnection
from lib.recipe_repository import RecipeRepository

# Connect to database
connection = DatabaseConnection()
connection.connect()

# Seed with seed data
connection.seed("seeds/recipes.sql")

# Retrieve the recipes
recipe_repo = RecipeRepository(connection)
recipes = recipe_repo.all()

# Print list of recipes
for recipe in recipes:
    print(recipe)