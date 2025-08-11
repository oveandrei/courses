# Pitfall: Modifying a list while iterating
nums = [1, 2, 3, 4]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print(nums)  
# Output: [1, 3] — BUT it skipped 4 because indexes shifted!

# Safe approach: iterate over a copy or use list comprehension
nums = [1, 2, 3, 4]
nums = [n for n in nums if n % 2 != 0]
print(nums)  # [1, 3]
