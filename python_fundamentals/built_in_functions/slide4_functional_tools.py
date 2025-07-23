
nums = [1, 2, 3, 4, 5]

# Double each number
doubled = list(map(lambda x: x* 2, nums)) # [2, 4, 6, 8, 10]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums)) # [2, 4]
