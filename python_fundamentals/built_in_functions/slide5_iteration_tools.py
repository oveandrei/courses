
'''zip()'''

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

combined = list(zip(names, scores))
print(combined) # [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Unzippint with zip(*zipped)
zipped = list(zip(['a', 'b'], [1, 2]))
names, values = zip(*zipped)

print(names) # ('a', 'b')
print(values) # (1, 2)

# common gotcha -- Behavior on Uneven Lenghts (zip() truncates)
names = ["Alice", "Bob"]
scores = [85, 92, 78]

print(list(zip(names, scores)))
# [('Alice', 85), ('Bob', 92)]  ← Notice 78 is dropped!

'''enumerate()'''
for idx, name in enumerate(names, start = 1):
    print(f"{idx}. {name}")
# 1. Alice
# 2. Bob
# 3. Charlie
