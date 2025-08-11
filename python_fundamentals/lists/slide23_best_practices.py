'''Use List Comprehensions for Clarity and Performance'''
nums = [1, 2, 3, 4, 5]

# Instead of using a loop to create squares:
squares = []
for n in nums:
    squares.append(n**2)  # Append the square of n

# Use a list comprehension for the same result:
squares = [n**2 for n in nums]  # Cleaner and more Pythonic

print(squares)  # Output: [1, 4, 9, 16, 25]

'''Avoid Modifying Lists While Iterating'''
nums = [1, 2, 3, 4]

# Problematic way: modifying list during iteration
for n in nums:
    if n % 2 == 0:
        nums.remove(n)  # Removing items shifts indices and causes skips

print(nums)  # Output might be unexpected: [1, 3]

#  Safe way: create a new filtered list instead
nums = [1, 2, 3, 4]
filtered = [n for n in nums if n % 2 != 0]  # Keep only odd numbers
print(filtered)  # Output: [1, 3]

'''Use copy() or deepcopy() to Avoid Shared References'''
import copy

original = [[1, 2], [3, 4]]
shallow_copy = original.copy()
deep_copy = copy.deepcopy(original)

shallow_copy[0].append(99)  # Affects original because inner lists are shared
print(original)  # Output: [[1, 2, 99], [3, 4]]

deep_copy[1].append(100)    # Does NOT affect original
print(original)  # Output remains: [[1, 2, 99], [3, 4]]

'''Prefer collections.deque for Queues and Stacks When Performance Matters'''
from collections import deque

queue = deque()
queue.append('A')  # Enqueue
queue.append('B')
print(queue.popleft())  # Dequeue 'A' efficiently
