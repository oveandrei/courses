'''gc (Garbage collector)'''
import gc

# Force garbage collection manually
unreachable = gc.collect()
print(f"Unreachable objects collected: {unreachable}")

# View current garbage collector thresholds
print("GC thresholds", gc.get_threshold())

# Debug: track objects
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

# Example: detect circular reference
class Node:
    def __init__(self):
        self.ref = self

node = Node()
del node # Creates a circular reference
gc.collect() # Will no detect and clean it
# gc.collect() is useful in memory leak investigation or benchmarking cleanup performance.


'''weakref'''
import weakref

class Data:
    def __init__(self, value):
        self.value = value

# Create an object
obj = Data(42)

# Create a weak reference to it
ref = weakref.ref(obj)

print(ref()) # <__main__.Data object at...>

# Delete the original object
del obj

# Weak reference is now dead
print(ref()) # None
# Useful in  caches: if the object is no longer used elsewhere, it dissapears automatically - freeing memory.