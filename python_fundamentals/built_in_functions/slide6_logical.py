''' These functions are clean, fast replacements for loops like:
for x in items:
    if not x: return False
'''

nums = [1, 2, 3, 0]

print(all(nums)) # False - 0 is Falsy
print(any(nums)) # True - at least one value is truthy

conditions = [x > 0 for x in nums]
print(all(conditions)) # False because of 0
