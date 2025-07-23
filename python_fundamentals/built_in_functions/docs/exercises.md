# A list of exercises in order to strengthen your learning

## Functional Tools

**Functions:** `map()`, `filter()`, `reduce()`

Given a list of integers `[1, 2, 3, 4, 5]`:

1. Use `map()` to create a list where each number is squared.
2. Use `filter()` to keep only even numbers from the original list.
3. Use `reduce()` _import from functools_ to calculate the product of all numbers in the list.

## Iteration Helpers

**Functions:** `zip()`, `enumerate`

Given two lists:

* `names = ["Anna", "Bob", "Cathy"]`
* `ages = [28, 35, 22]`

1. Use `zip()` to pair names with ages and print them as `Name: Anna, Age: 28`.
2. Use `enumerate()` on the `names` list starting at 1 and print index and name as `1. Anna`.

## Logical and Sorting

**Functions:** `all()`, `any()`, `sorted()`

Given `words = ["apple", "", "banana", None]`

1. Use `all()` to check if all elements are truthy.
2. Use `any()` to check if any element is `None`.
3. Sort the list `words` ignoring `None` values (filter them out first) and print the sorted result.

## Code Execution

**Functions:** `eval()`, `exec()`, `compile()`

1. Use `compile()` to compile the expression `"5+ 7 * 2"` and then use `eval()` to evaluate it.
2. Write a small Python code string that defines a function `greet(name)` printing `"Hello, {name}"` and run it with `exec()`.
3. Call `greet("World")` after executing the compiled code.

## Namespace Introspection

**Functions:** `dir()`, `vars()`, `locals()`, `globals()`

1. Create a class `Car` with attributes `make` and `model`.
2. Use `dir()` on an instance of `Car` to list all attributes.
3. Use `vars()` on the instance to get its `__dict__`.
4. Print `locals()` inside a function to show local variables.
5. Print `globals()` and check if `Car` is present.

## Type & Callable Checks

**Functions:** `type()`, `isinstance()`, `callable()`

1. Define a function `square(x)` and check if it is callable.
2. Check the type of a list and verify if it is an instance of `list`.
3. Use `isinstance()` to check if the number `5` is an instance of `int` or `float`.
4. Define a class `Foo` with a `__call__` method, create an instance, and verify it is callable.

## Dynamically Working with Objects

**Functions:** `hasattr()`, `getattr()`, `setattr()`, `delattr()`

1. Create a class `User` with attribute `username`.
2. Use `setattr()` to dynamically add an attribute `email`.
3. Use `hasattr()` to check if `email` exists.
4. Use `getattr()` to retrieve `username`.
5. Use `delattr()` to delete the `username` attribute and check with `hasattr()` again.

## Type Conversion Built-ins

**Functions:** `int()`, `str()`, `float()`, `bool()`, `complex()`

1. Write a function `save_int_convert(value, default)` that tries to convert `value` to an int and returns `default` if it fails (use `try-except`).
2. Convert the string `"False"` to a boolean - observe the result and explain why.
3. Create a complex number from two floats `3.5` and `-2.1` without using `complex()` constructor (hint: use `complex(real, imag)` explicitly).
4. Convert the integer `255` to its hexadecimal string representation using `str()` combined with `hex()`.

## Collection Constructors

**Functions:** `list()`, `tuple()`, `set()`, `dict()`, `frozenset()`

1. Given a generator expression producing numbers 1 through 5, convert it to a list and a tuple.
2. Create a dictionary from two lists: keys `["x", "y", "z"]` and values `[9, 8, 7]` uing `zip()` and `dict()`
3. Convert the string `mississippi` into a `frozenset` and explain why you cannot add elements to it.
4. Create a set from the list `[1, 2, 2, 3, 4]` and demonstrate that duplicates are removed.

## String Representation and Formatting

**Functions:** `repr()`, `ascii()`, `format()`

1. Print the `repr()` of a list containing string and integers: `["foo", 42, "bar"]`.
2. Use `ascii()` on the string `"naïve café"` and observe the output.
3. Format the number `12345.6789` to have a comma separators and thousands and two decimals places using `format()`.
4. Use `format()` with the format specifier to right-aligh the string `"test"` in a 10-character field.

## User Interaction

**Functions:** `print()`, `input()`

1. Write a program that asks for three numbers from the user, then prints their average rounded to two decimals.
2. Use `print()` to display the results in a single line, separated by commas.
3. Use the `end` parameter in `print()` to avoid automatic newlines and print a progress bar-like output (e.g., dots printed one after another).

## Advanced Data Access

**Functions:** `reversed()`, `slice()`, `memoryview()`

1. Use `reversed()` on a list of words `["one", "two", "three"]` and print them on separate lines.
2. Create a slice object that extracts every third element from a range of numbers 0 to 20 and apply it to a list.
3. Use `memoryview()` on a bytes object `b"hello world"` and modify one byte to uppercase "W" (check byte values before and after).

## Dynamic Import

**Functions:** `help()`, `__import__()`

1. Call `help()` on the built-in function `sorted` and summarize in your own words what it does.
2. Dynamically import the `random` module with the `__import__()` and use it to generate a random integer between 1 and 100.
3. Write a function `dynamic_import(module_name, func_name)` that imports a module by name and returns a function by name from that module.
