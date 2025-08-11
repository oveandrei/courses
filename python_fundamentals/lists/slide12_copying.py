import copy
a = [[1, 2], [3, 4]]
b = a.copy()
c = copy.deepcopy(a)
d = a

print(a is b) # False
print(a is c) # False
print(a is d) # True
