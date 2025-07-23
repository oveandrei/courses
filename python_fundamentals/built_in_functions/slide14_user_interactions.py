# Basic usage
print("Hello, world!")            # Hello, world!

# Multiple arguments and custom separator
print("A", "B", "C", sep="-")     # A-B-C

# Suppressing the newline
print("Loading...", end="")      
print("Done")                     # Output: Loading...Done

# Asking for input
name = input("What is your name? ")
print("Nice to meet you,", name)

# Always returns a string, even if you type a number!
age = input("Enter your age: ")
print("Age plus one:", int(age) + 1)
