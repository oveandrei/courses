'''Sequential Flow Example'''
print(1)
print(2)

'''Conditional Flow Example'''

animal = 'dog'
if animal == 'dog': # This if statement checks if the animal is a dog.
    print('This is a dog.')
elif animal == 'cat': # This elif statement gets executed if the animal is a cat.
    print("This is a cat.")
else:       # This else statement gets executed if the previous conditions are not met.
    print("This is neither a dog nor a cat.")


'''Iterative Flow Example'''

for number in range(5): # This for loop iterates over a range of numbers from 0 to 4.
    print(f"Iteration {number + 1}") # This line prints the current iteration number.

number = 0
while number < 5: # This while loop continues as long as the number is less than 5.
    number += 1 # This line increments the number by 1 in each iteration.
    if number == 2:
        print("Reached number 2") # This way we altered the normal flow by adding a condition.
        continue
    if number == 4:
        print("Reached number 4, breaking loop")
        break # This line breaks the loop when the number reaches 4. This way we altered the normal flow by breaking the loop.
    print(f"While loop iteration: {number}") # This line prints the current iteration number.


'''Function Calls Example'''

def greet(name):
    print(f"Hello, {name}") # This function prints a greeting message.

# In order to activate the function, we need to call it with the 'name' argument inside of the call. Otherwise it won't execute.
greet("Alice") # Calls the greet function with "Alice" as an argument


'''Exception Handling Example'''

try:
    result = 10 / 0 # Attempts to divide by zero, which will raise an exception (error).
except ZeroDivisionError as e: # This block catches the ZeroDivisionError error.
    print(f"An error occurred: {e}")
finally: # This executes no matter what in the end
    print("This block always executes, regardless of whether an exception occured or not.")