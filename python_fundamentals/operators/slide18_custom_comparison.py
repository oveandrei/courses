
class Person:
    def __init__(self, name, age):
        # Initialize a person with name and age
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        # Define equality: two people are equal if their age is equal
        return self.age == other.age

    def __lt__(self, other):
        # Define less-than: compare people based on age
        return self.age < other.age
    
    def __str__(self):
        # Define how the object is printed (human-readable string)
        return f"{self.name} ({self.age})"
    
# Create a list of people
people = [
    Person('Alice', 30),
    Person("Bob", 25),
    Person("Charlie", 35)
]

# Sort the list based on age using the overloaded < operator
people.sort()

# Print the sorted list
for person in people:
    print(person)

'''Expected output:
Bob (25)
Alice (30)
Charlie (35)
'''