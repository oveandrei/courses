# Membership
fruits = ['apple', 'banana', 'cherry']
print("banana" in fruits) # True
print("mango" not in fruits) # True

# Identity
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y) # True (same object)
print(x == z) # True (equal values)
print(x is z) # False (different objects)
