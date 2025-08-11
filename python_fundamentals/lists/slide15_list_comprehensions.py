squares = [x**2 for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]
matrix = [[i*j for j in range(3)] for i in range(3)]

print(squares) # [0, 1, 4, 9, 16]
print(evens) # [0, 2, 4, 6, 8]
print(matrix) # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
