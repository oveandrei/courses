lst = [1, 2]
lst.append([3, 4])   # Adds list as a single element -> [1, 2, [3, 4]]      # type: ignore
lst.extend([5, 6])   # Adds elements individually -> [1, 2, [3, 4], 5, 6]
lst.insert(1, 10)    # Inserts at index 1 -> [1, 10, 2, [3, 4], 5, 6]
