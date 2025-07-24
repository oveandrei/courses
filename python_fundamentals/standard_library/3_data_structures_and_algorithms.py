'''array'''

import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4])

# Append an element
arr.append(5)

# Access an element
print(arr[2]) # 3

# Output array
print(arr) # array('i', [1,2,3,4,5])


'''collections'''

from collections import deque, Counter, defaultdict, namedtuple

# deque example
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq) # deque([0, 1, 2, 3, 4])

# Counter example
c = Counter("banana")
print(c) # Counter({'a': 3, 'n': 2, 'b': 1})

# defaultdict example
dd = defaultdict(int)
dd['a'] += 1
print(dd['a']) # 1
print(dd['b']) # 0 (default int value)

# namedtuple example
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y) # 1 2


'''reprlib'''

import reprlib

# Large list that needs truncating
long_list = list(range(1000))

# Create abbreviated string representation
print(reprlib.repr(long_list))
# Output: [0, 1, 2, 3, 4, 5 ...... 998, 999]


'''pprint'''

import pprint

# Complex nested structure
data = {
    'fruits' : ['apple', 'banana', 'cherry'],
    'vegetables': ['lettuce', 'carrot', 'onion'],
    'grains': ['rice', 'wheat', 'quinoa']
}
# Pretty-print
pprint.pprint(data, width=40)


'''enum'''

from enum import Enum

class Status(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3

# Usage
print(Status.APPROVED) # Status.APPROVED
print(Status.APPROVED.name) # 'APPROVED'
print(Status.APPROVED.value) # 2


'''functools'''
from functools import lru_cache, partial, reduce

# lru_cache example
@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
print(fib(10)) # 55

# partial example
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5)) # 25

# reduce example
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product) # 24


'''itertools'''

import itertools

# chain: Flatten multiple iterables
a = [1, 2]
b = [3, 4]
print(list(itertools.chain(a, b))) # [1, 2, 3, 4]

# count: Infinite counte (use with caution)
counter = itertools.count(start=10, step=2)
print(next(counter)) # 10
print(next(counter)) # 12

# combinations: All unique pairs
letters = ['A', 'B', 'C']
print(list(itertools.combinations(letters, 2)))
# [('A', 'B'), ("A", "C"), ("B", "C")]

# product: Cartesian product
colors = ['red', 'green']
sizes = ['S', 'M']
print(list(itertools.product(colors, sizes)))
# [('red', 'S'), ('red', 'M'), ('green', 'S'), ('green', 'M')]

# groupby: Group consecutive values
data = [('a', 1), ('a', 2), ('b', 3)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))
# a [('a', 1), ('a', 2)]
# b [('b', 3)]


'''operator'''

import operator

# Basic operator functions
print(operator.add(2, 3)) # 5
print(operator.mul(4, 5)) # 20
print(operator.pow(2, 3)) # 8

# itemgetter: Used to extract items by index
data = [('a', 2), ('b', 1), ('c', 3)]
get_second = operator.itemgetter(1)
print(get_second(data[0])) # 2

# Sort list of tuples by second items
sorted_data = sorted(data, key=operator.itemgetter(1))
print(sorted_data) # [('b', 1), ('a', 2), ('c', 3)]

# attrgetter: Extract object attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person('Alice', 30), Person('Bob', 25)]
sorted_people = sorted(people, key=operator.attrgetter('age'))
print([p.name for p in sorted_people]) # ['Bob', 'Alice']
