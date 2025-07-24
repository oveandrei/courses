
'''Indexing example'''
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Accessing elements by index
print(fruits[1]) # Output: banana
# Negative indexing example
print(fruits[-1]) # Output: elderberry

'''Slicing example'''
print(fruits[1:4]) # Output: ['banana', 'cherry', 'date']

'''Slicing with step example'''
print(fruits[::2]) # Output ['apple', 'cherry', 'elderberry']

'''Slicing with negative step example'''
print(fruits[::-1]) # Output ['elderberry', 'date', 'cherry', 'banana', 'apple']

'''Slicing with start, stop, and step example'''
print(fruits[1:5:2]) # Output: ['banana', 'date']

'''Iteration example'''
for fruit in fruits:
    print(fruit)

'''Membership test example'''
print('banana' in fruits) # True
print('fig' in fruits) # False

'''Length example'''
print(len(fruits)) # 5

'''Nested collection example'''
nested_fruits = [['apple', 'banana'], ['cherry', 'date'], ['elderberry']]
# Accessing nested elements
print(nested_fruits[0][1]) # Banana
print(nested_fruits[0]) # ['apple', 'banana']

'''List comprehension example'''
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]