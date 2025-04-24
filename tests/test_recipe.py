from lib.recipe import Recipe

'''
When recipe is added, 
The details are saved within __init__
'''

def test_recipe_is_saved():
    recipe = Recipe(1, 'Ratatouille', '55 mins', 4)
    assert recipe.name == 'Ratatouille'
    assert recipe.cooking_time == '55 mins'
    assert recipe.rating == 4

'''
When str(recipe) is called,
A formatted string representing the attributes within the recipe is returned
'''

def test_recipe_is_formatted_nicely():
    recipe = Recipe(1, 'Ratatouille', '55 mins', 4)
    assert str(recipe) == "Recipe(1, Ratatouille, 55 mins, 4)"

'''
When comparing two recipes, 
True is returned is recipes have identical attributes
'''
def test_comparing_two_recipes_returns_correct_result():
    recipe1 = Recipe(1, 'Ratatouille', '55 mins', 4)
    recipe2 = Recipe(1, 'Ratatouille', '55 mins', 4)
    recipe3 = Recipe(2, 'Beef Stew', '202 mins', 3)
    assert recipe1 == recipe2
    assert recipe2 != recipe3