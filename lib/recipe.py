class Recipe:
    
    def __init__(self, id, name, cooking_time, rating):
        self.id = id
        self.name = name
        self.cooking_time = cooking_time
        self.rating = rating

    # String representation of recipe
    def __repr__(self):
        return f"Recipe(id: {self.id}, name: {self.name}, cooking time: {self.cooking_time}, rating: {self.rating})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__