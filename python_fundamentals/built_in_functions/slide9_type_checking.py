x = 42
y = "hello"

# type() returns the exact type of the object
print(type(x))         # Output: <class 'int'>
print(type(y))         # Output: <class 'str'>

# isinstance() checks if object matches a given type
print(isinstance(x, int))          # True
print(isinstance(y, (int, float))) # False — not a number