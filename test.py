import itertools
l = [False, True]
[list(i) for i in itertools.product(l, repeat=3)]
