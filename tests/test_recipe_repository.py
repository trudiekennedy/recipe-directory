from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

'''
When I call RecipeRepository #all
I get a list recipe objects representing the seed data
'''
def test_get_all_recipes(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipes = repository.all()

    assert recipes == [
        Recipe(1, 'Salmon in a Soy and Ginger Sauce', 35, 5),
        Recipe(2, 'Tuna & Rice', 75, 4),
        Recipe(3, 'Mince & Tatties', 60, 2),
        Recipe(4,'Chicken with Mushroom and White Wine Sauce', 45, 3),
        Recipe(5,'Chicken Fajitas', 30, 4),
    ]

'''
When I call RecipeRepository#find 
I get a single recipe representing the seed data
'''

def test_get_single_recipe(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipe = repository.find(3)
    assert recipe == Recipe(3, 'Mince & Tatties', 60, 2)
