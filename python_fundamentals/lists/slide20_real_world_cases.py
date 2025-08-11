'''Storing & Processing Data'''
temperatures = [22.5, 19.0, 23.7]
avg_temp = sum(temperatures) / len(temperatures)
print(f"Average: {avg_temp:.1f}°C")
# Great for datasets where order matters

'''Representing Game Inventories'''
inventory = ["sword", "shield", "potion"]
inventory.append("bow")
print(inventory)
# Easily add/remove items during gameplay

'''Single Data Pipelines'''
words = ["apple", "banana", "cherry"]
capitalized = [w.capitalize() for w in words]
print(capitalized)
# Ideal for quick transformations with list comprehensions
