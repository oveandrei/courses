nums = [3, 1, 2]
nums.sort()
print(sorted(nums, reverse=True)) # [3, 2, 1]
words = ["avocado", "apple", "banana"]
words.sort(key=len)
print(words) # ['apple', 'banana', 'avocado']
