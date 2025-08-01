"""1. Using is vs == improperly"""
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # True - values are equal
print(a is b) # False - different objects in memory

"""2. Mutable default arguments in operator overloads"""
class Counter:
    def __init__(self, nums=[]):
        self.nums = nums
    
    def __add__(self, other):
        # Problem: modifies original list in-place!
        self.nums += other.nums
        return self
# Fix: Use .copy() or + to create a new list instead of modifying in-place

"""3. Forgetting parentheses in chained comparisons"""
x = 3
print(1 < x < 5) # True - chained comparison
print((1 < x) and (x < 5)) # Equivalent
