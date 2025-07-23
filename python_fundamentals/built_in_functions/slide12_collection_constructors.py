# Create a list from a string
print(list("abc"))         # ['a', 'b', 'c']

# Convert list to tuple
print(tuple([1, 2, 3]))     # (1, 2, 3)

# Create set from a list (removes duplicates)
print(set([1, 2, 2, 3]))    # {1, 2, 3}

# Create dictionary from pairs
print(dict([("a", 1), ("b", 2)]))  # {'a': 1, 'b': 2}

# Create a frozenset (immutable set)
f = frozenset([1, 2, 2, 3])
print(f)                   # frozenset({1, 2, 3})

# Caution: {} is an empty dict, not an empty set!
print(type({}))            # <class 'dict'>
