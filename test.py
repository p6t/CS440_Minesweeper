import itertools
from itertools import product
truefalse = [False, True]
allPossibilities = (list(itertools.product(truefalse, repeat=2)))

print(allPossibilities)
