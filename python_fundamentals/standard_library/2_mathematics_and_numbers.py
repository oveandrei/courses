'''1. Math'''

import math

# Example 1: square root
print(math.sqrt(16)) # Output: 4.0

# Example 2: Trigonometric functions
print(math.sin(math.pi / 2)) # Output 1.0

# Example 3: Ceiling and floor
print(math.ceil(2.3)) # Output 3
print(math.floor(2.7)) # Output: 2

# Example 4: Logarithm
print(math.log(100, 10)) # Output 2.0


'''2. Random'''

import random

# Example 1: Random float between 0 and 1
print(random.random()) # e.g., 0.643...

# Example 2: Random integer between 1 and 10
print(random.randint(1, 10)) # e.g., 7

# Example 3: Choose a random element
print(random.choice(['apple', 'banana', 'cherry'])) # e.g., 'cherry'

# Example 4: Shuffle a list
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items) # Shuffled list

# Example 5: Reproductibility with seed
random.seed(42)
print(random.random()) # Always the same if seed is fixed


'''3. statistics'''

import statistics

data = [1, 2, 3, 4, 5]

# Example 1: Mean (average)
print(statistics.mean(data)) # 2.833...

# Example 2: Median
print(statistics.median(data)) # 2.5

# Example 3: Mode
print(statistics.mode(data)) # 2 (most frequent)

# Example 4: Standard deviation
print(statistics.stdev(data)) # e.g., 1.47


'''4. decimal'''

from decimal import Decimal, getcontext

# Set precision
getcontext().prec = 5

# Example 1: Basic arithmetic
a = Decimal('0.1')
b = Decimal('0.2')
print(a + b) # 0.3 (precise!)

# Example 2: without Decimal
print(0.1 + 0.2) # 0.300000000004 ( imprecise due to binary float)


'''5. heapq'''

import heapq

# Example 1: Create a heap
numbers = [5, 3, 8, 1]
heapq.heapify(numbers) # transforms list into a min-heap
print(numbers) # [1, 3, 8, 5]

# Example 2: Add an element
heapq.heappush(numbers, 2)
print(numbers) # [1, 2, 8, 5, 3]

# Example 3: Remove smallest element
print(heapq.heappop(numbers)) # 1


'''6. bisect'''

import bisect

# Must be a sorted list
scores = [10, 20, 30, 40, 50]

# Example 1: Find position to insert
index = bisect.bisect_left(scores, 25) # Finds insertion point for 25
print(index) # 2

# Example 2: Insert while maintaining order
bisect.insort(scores, 25)
print(scores) # [10, 20, 25, 30, 40, 50]