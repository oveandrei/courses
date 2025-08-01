class Point:
    def __init__(self, x, y):
        # Initialize a point with x and y coordinates
        self.x = x
        self.y = y

    def __add__(self, other):
        # Define how two Point objects are added using the '+' operator
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        # Define how the object is displayed when printed
        return f"({self.x}, {self.y})"

# Create two Point instances
p1 = Point(1, 2)
p2 = Point(3, 4)

# Use the overloaded '+' operator to add the two points
result = p1 + p2

# Print the res
print(result)  # Output: (4, 6)