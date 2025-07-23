
'''Use built-ins before external libraries'''
# Prefer this:
squared = list(map(lambda x: x**2, range(5)))

# Over external libraries unless truly necessary

'''Prefer readable & idiomatic usage'''
# Clear and Pythonic
total = sum(numbers) # type: ignore

# Less readable
total = 0
for num in numbers:  # type: ignore
    total += num

'''Avoid overusing obscure built-ins'''
# __import__ is powerful, but rarely needed directly
mod = __import__('math')
print(mod.sqrt(25))

# prefer import math

'''Avoid shadowing built-ins'''
#  Bad practice: naming a variable after a built-in
list = [1, 2, 3]     # Now you can't use the list() function!
