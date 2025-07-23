# Define a simple class
class Person:
    def __init__(self, name):
        self.name = name

# Create an instance
p = Person("Alice")

# dir() lists attributes and methods of an object
# Includes inherited and dunder methods (like __init__, __str__, etc.)
print(dir(p))

# vars() returns the instance’s __dict__ (its attributes as a dict)
print(vars(p))  # Output: {'name': 'Alice'}

# locals() returns a dictionary of the local symbol table
# This will include all local variables in the current scope
print(locals())  # Outputs a large dict with everything in local scope

# globals() returns a dictionary of the global namespace
# Useful for accessing or checking variables defined at the top level
print('Person' in globals())  # True — 'Person' class is defined globally