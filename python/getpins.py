# kata: https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

# NOTE: best solution

from itertools import product

# pad:
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
#    0

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]

# from textwrap import wrap
# 
# adj = {
#     "1": [2, 4],
#     "2": [1, 3, 5],
#     "3": [2, 6],
#     "4": [1, 5, 7],
#     "5": [2, 4, 6, 8],
#     "6": [3, 5, 9], 
#     "7": [4, 8],
#     "8": [0, 5, 7, 9],
#     "9": [6, 8],
#     "0": [8]
# }
# 
# def get_pins(obs):
#     pins = [obs]
# 
#     digits = wrap(obs, 1)
#     control = digits.copy()
# 
#     while ...:
#         digits = wrap(obs, 1)
#         for possibilitie in adj[d]:
#             print("".join(digits))
#             digits[i] = str(possibilitie)
#             pins.append("".join(digits))
# 
#     return pins
