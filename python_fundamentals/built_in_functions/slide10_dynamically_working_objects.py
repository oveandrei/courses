class Person:
    def __init__(self):
        self.name = "Alice"

p = Person()

# hasattr checks if 'name' exists
print(hasattr(p, "name"))      # True

# getattr retrieves 'name'
print(getattr(p, "name"))      # Alice

# getattr with fallback for non-existent attribute
print(getattr(p, "age", 30))   # 30

# setattr creates/updates 'age'
setattr(p, "age", 25)
print(p.age) # type: ignore     # 25

# delattr deletes 'name'
delattr(p, "name")
print(hasattr(p, "name"))      # False
