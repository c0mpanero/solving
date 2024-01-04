# kata: https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

from math import floor

def cakes(recipe, available):
    if len(recipe.keys()) > len(available.keys()):
        return 0
    
    how_much = []
    
    for k, v in recipe.items():
        try:
            how_much.append(floor(
                available[k] / v
            ))
        except KeyError:
            return 0

    return  min(how_much)
