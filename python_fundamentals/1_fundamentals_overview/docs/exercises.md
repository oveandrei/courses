# A set of exercises in order to strengthen the learning

## Python Basics

### Introduction to Python

**Minimum Requirements Product (MRP):**  
Write a short script that prints out a welcome message and lists 3 key benefits of Python.

**Requirements:**

1. The user has to use the `print()` function.
2. The user needs to list at least 3 advantages of Python from the text.

**Required usage:**

* `print`, `str`

---

## Program Flow

### Programming Flow Types

**Minimum Requirements Product (MRP):**  
Create a program that simulates an ATM check using branching, looping, and function calls.

**Requirements:**

1. The user has to define a function called `check_balance()`.
2. The user needs to use `if`, `while`, and `break` to control the flow of the ATM.
3. The ATM should keep prompting until a correct PIN is entered, then call the function.

**Required usage:**

* `def`, `if`, `while`, `break`

---

## Data Types

### Numeric, Text, Boolean, None, Collections

**Minimum Requirements Product (MRP):**  
Create a Python script that defines a profile dictionary containing name, age, is_student, favorite numbers, and no_middle_name.

**Requirements:**

1. The user must declare at least one variable of each type: `str`, `int`, `bool`, `None`, `list`.
2. The user needs to store all this data in a `dict`.

**Required usage:**

* `str`, `int`, `bool`, `None`, `list`, `dict`, `type()`

---

## Variables

### Variable Rules and Naming

**Minimum Requirements Product (MRP):**  
Create a script where you define 3 variables with legal names and assign them different data types.

**Requirements:**

1. The user has to follow Python naming rules.
2. The user must use `print()` to output the variable name and value.
3. The user needs to show that variable types can be changed.

**Required usage:**

* `print`, `type`, `str`, `int`, `float`

---

## Operators

### Arithmetic, Comparison, Logical, Membership

**Minimum Requirements Product (MRP):**  
Write a small calculator that checks if two numbers are equal, greater, or smaller, and prints if both are inside a list.

**Requirements:**

1. The user has to use arithmetic, comparison, logical, and membership operators.
2. The user must take two variables and perform at least 3 types of operations on them.

**Required usage:**

* `+`, `-`, `==`, `>`, `<`, `in`, `and`, `or`

---

## Functions

### Defining and Using Functions

**Minimum Requirements Product (MRP):**  
Create a function that greets a user by name and returns the length of their name.

**Requirements:**

1. The user has to define a function using `def`.
2. The function must accept a parameter and return a result.
3. The user needs to call the function and print the result.

**Required usage:**

* `def`, `return`, `len`, `print`

---

### Lambda and Built-in Functions

**Minimum Requirements Product (MRP):**  
Create a lambda function to square a number and use a built-in function to apply it to a list.

**Requirements:**

1. The user must define a lambda function.
2. The user has to apply it using the `map()` function to a list of numbers.
3. The user must print the results.

**Required usage:**

* `lambda`, `map`, `list`, `print`

---

## Object-Oriented Programming (OOP)

### Classes and Objects

**Minimum Requirements Product (MRP):**  
Create a class `Person` that has attributes `name` and `age` and a method `greet()` that prints a greeting.

**Requirements:**

1. The user has to define a class using `class`.
2. The user needs to implement the `__init__` method and define attributes.
3. The user must create an object from the class and call the `greet()` method.

**Required usage:**

* `class`, `__init__`, `self`, method call

---

### Inheritance and Encapsulation

**Minimum Requirements Product (MRP):**  
Create a `Vehicle` class and a `Car` subclass that inherits from it and adds its own method.

**Requirements:**

1. The user has to define a base class and subclass.
2. The user must override or extend functionality.
3. The user should encapsulate a variable using a single underscore.

**Required usage:**

* `class`, `super()`, `_protected_var`, inheritance

---

### Special Methods and Polymorphism

**Minimum Requirements Product (MRP):**  
Create two different classes (`Dog`, `Cat`) that both implement a `speak()` method. Call them in a loop and demonstrate polymorphism.

**Requirements:**

1. The user must define two classes with a shared method name.
2. The user needs to use a loop to call `speak()` on each object.
3. Optionally, override `__str__` for better print output.

**Required usage:**

* `__str__`, method overriding, loop, `print`

---

## Collections

### Collection Types and Access

**Minimum Requirements Product (MRP):**  
Create a list, tuple, set, and dictionary representing the same group of fruits, and demonstrate how to access elements.

**Requirements:**

1. The user must create one of each: list, tuple, set, and dict.
2. The user has to access an element from the list and tuple by index.
3. The user needs to access a value from the dict using its key.

**Required usage:**

* `list`, `tuple`, `set`, `dict`, indexing, key access

---

### Collection Manipulation

**Minimum Requirements Product (MRP):**  
Create a shopping list using a list, then perform add, remove, and update operations.

**Requirements:**

1. The user has to add items using `.append()`, `.insert()`, or `.extend()`.
2. The user must remove an item using `.remove()` or `.pop()`.
3. The user must change an item by index.

**Required usage:**

* `list`, `.append()`, `.remove()`, index assignment

---

### Nested and Combined Collections

**Minimum Requirements Product (MRP):**  
Create a dictionary where each value is a list of tasks for a different day of the week.

**Requirements:**

1. The user must define a nested data structure (dict of lists).
2. The user has to add a task to Monday and print all Monday tasks.
3. The user needs to iterate over all tasks for all days.

**Required usage:**

* `dict`, `list`, indexing, `for` loop

---

### Built-in Functions with Collections

**Minimum Requirements Product (MRP):**  
Create a list of numbers and demonstrate sorting, summing, and finding the maximum value.

**Requirements:**

1. The user has to create a numeric list.
2. The user must use `sorted()`, `sum()`, and `max()` functions.
3. The user must print the results clearly.

**Required usage:**

* `sorted`, `sum`, `max`, `print`

---

## String Manipulation

### Basic String Operations

**Minimum Requirements Product (MRP):**  
Create a program that takes a full name as a string and formats it as "LASTNAME, Firstname".

**Requirements:**

1. The user must use `.split()` and `.upper()` or `.capitalize()`.
2. The user has to join the formatted parts into a final string.
3. The user needs to print the result.

**Required usage:**

* `str.split()`, `str.upper()`, `str.capitalize()`, `str.join()`

---

### Cleaning and Validating Strings

**Minimum Requirements Product (MRP):**  
Ask the user to enter a username and check if it's valid (non-empty, alphabetic only, no spaces).

**Requirements:**

1. The user must use `.strip()` to clean input.
2. The user needs to check with `.isalpha()` and print a validation message.
3. The program must reject invalid inputs with a clear message.

**Required usage:**

* `input`, `str.strip()`, `str.isalpha()`, `if`

---

## Error Handling

### Try-Except Basics

**Minimum Requirements Product (MRP):**  
Write a program that asks the user for two numbers and divides them, handling division by zero.

**Requirements:**

1. The user has to use a `try-except` block.
2. The user must catch `ZeroDivisionError` and show a friendly error message.
3. The result must be printed if no error occurs.

**Required usage:**

* `try`, `except`, `ZeroDivisionError`, `input`, `int`

---

### Else, Finally, and Raising Errors

**Minimum Requirements Product (MRP):**  
Ask for a user's age, validate it, and raise an error if it's negative.

**Requirements:**

1. The user must raise a `ValueError` if the input is invalid.
2. The user needs to use `try`, `except`, `else`, and `finally`.
3. A message must be shown whether an error occurred or not.

**Required usage:**

* `try`, `except`, `raise`, `else`, `finally`, `ValueError`

---

## Importing & Libraries

### Standard and External Libraries

**Minimum Requirements Product (MRP):**  
Use the `math` library to calculate the square root and area of a circle given a radius.

**Requirements:**

1. The user has to import `math` using a standard `import` statement.
2. The user must use `math.sqrt()` and `math.pi`.
3. The user needs to print the results clearly.

**Required usage:**

* `import math`, `math.sqrt`, `math.pi`

---

### Import Variants and Custom Modules

**Minimum Requirements Product (MRP):**  
Create a small utility module named `helper.py` with a function that returns the square of a number, and import it in another file.

**Requirements:**

1. The user has to define a file `helper.py` with a function `square(x)`.
2. The user must import and use the function in another script.
3. The import must use `from helper import square`.

**Required usage:**

* `def`, `return`, `from ... import`, custom module

---

## File Handling

### Reading and Writing Files

**Minimum Requirements Product (MRP):**  
Create a script that writes user input to a file and then reads the content back.

**Requirements:**

1. The user must use `with open()` to write and read safely.
2. The input must be written in a file called `notes.txt`.
3. The contents must be read and printed line by line.

**Required usage:**

* `with open`, `"w"`, `"r"`, `print`, `input`

---

### File Existence and Deletion

**Minimum Requirements Product (MRP):**  
Check if a file named `data.txt` exists, delete it if it does, and print a message.

**Requirements:**

1. The user must use `os.path.exists()` to check for file presence.
2. The user needs to use `os.remove()` to delete it.
3. A confirmation message must be shown after deletion.

**Required usage:**

* `import os`, `os.path.exists`, `os.remove`, `print`

---
