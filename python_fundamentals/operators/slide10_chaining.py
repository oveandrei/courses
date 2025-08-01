# Assignment chaining
a = b = c = 5
print(a, b, c) # 5 5 5

# Mutable objects caution
list1 = [1, 2, 3]
list2 = list1 # Both names point to same list
list2.append(4)

print(list1, list2) # [1, 2, 3, 4] [1, 2, 3, 4]

# Correct way: copy the list
import copy

list3 = copy.copy(list1)
list3.append(5)

print(list1, list3) # [1, 2, 3, 4] [1, 2, 3, 4 ,5]
