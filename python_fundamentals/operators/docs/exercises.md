# Operators Exercises

## Arithmetic Operators

**MRP:**

Create a simple calculator that can perform addition, subtraction, multiplication, division, floor division, modulus, and exponentiation.

**Requirements:**

1. Take two numeric inputs from the user.
2. Perform and display all arithmetic operations.

**Required Usage:**

* `+`, `-`, `*`, `/`, `//`, `%`, `**`

---

## Special Arithmetic Behavior

**MRP:**

Build a script that demonstrates Python’s arithmetic precedence using a combination of operations.

**Requirements:**

1. Define at least three expressions with mixed operators.
2. Show results with and without parentheses for comparison.

**Required Usage:**

* Operator precedence (`**`, `*`, `/`, `+`, `-`)
* Parentheses

---

## Comparison Operators

**MRP:**

Write a program that compares two user-provided values and outputs various comparison results.

**Requirements:**

1. Input two values from the user.
2. Display the result of each comparison operator.

**Required Usage:**

* `==`, `!=`, `<`, `>`, `<=`, `>=`

---

## Comparison Chaining and Python Idioms

**MRP:**

Check if a number falls within a given range using comparison chaining.

**Requirements:**

1. Input a number and define a lower and upper bound.
2. Use both standard logic and chained comparison to validate the result.

**Required Usage:**

* Chained comparisons (e.g., `low < x < high`)
* Logical `and`

---

## Assignment Operators

**MRP:**

Create a counter script that performs incremental changes to a variable using assignment operators.

**Requirements:**

1. Start with a variable initialized to zero.
2. Modify it using compound assignment at least five times.

**Required Usage:**

* `+=`, `-=`, `*=`, `/=`, `**=`

---

## Use Cases, Chaining, and Cautionary Tips

**MRP:**

Demonstrate the effects of assignment chaining with mutable and immutable types.

**Requirements:**

1. Assign a value to multiple variables in one line.
2. Show what happens when modifying one variable (for both a number and a list).

**Required Usage:**

* Assignment chaining
* `list.copy()` or `copy.deepcopy()`

---

## Logical Operators

**MRP:**

Build a condition checker that evaluates multiple user-defined boolean conditions using logic.

**Requirements:**

1. Define three boolean expressions.
2. Combine them using `and`, `or`, and `not`.

**Required Usage:**

* `and`, `or`, `not`

---

## Short-Circuit Behavior

**MRP:**

Create a script that demonstrates short-circuit evaluation using functions.

**Requirements:**

1. Define two functions that return boolean values and print when they're called.
2. Combine them using `and` and `or` to show how evaluation stops early.

**Required Usage:**

* Short-circuiting with `and` and `or`
* Function calls inside conditions

---

## Bitwise Operators

**MRP:**

Write a script that shows the result of different bitwise operations between two integers.

**Requirements:**

1. Define two integer variables.
2. Apply all bitwise operators and print the binary results.

**Required Usage:**

* `&`, `|`, `^`, `~`, `<<`, `>>`

---

## Practical Bitwise Use Cases

**MRP:**

Build a permission system using bitwise flags.

**Requirements:**

1. Define READ, WRITE, and EXECUTE flags using binary.
2. Assign permissions to a user and modify them using bitwise logic.

**Required Usage:**

* Bitwise flags with `|`, `&`, `^`, `~`
* Binary representation (e.g., `0b001`, `bin()`)

---

## Membership and Identity Operators

**MRP:**

Create a script that tests both identity and membership logic on various data types.

**Requirements:**

1. Use `is` and `is not` to compare object identities.
2. Use `in` and `not in` with lists and strings.

**Required Usage:**

* `is`, `is not`
* `in`, `not in`

---

## Operator Precedence and Associativity

**MRP:**

Write a script with several complex expressions to highlight how precedence and associativity affect evaluation.

**Requirements:**

1. Build expressions that use multiple operators with varying precedence.
2. Demonstrate differences when grouping expressions with parentheses.

**Required Usage:**

* Mixed operators (`+`, `*`, `**`, etc.)
* Parentheses for grouping

---

## Custom Operators via Magic Methods

**MRP:**

Define a class that supports custom addition and equality comparison using magic methods.

**Requirements:**

1. Create a class with `__add__` and `__eq__` methods.
2. Instantiate objects and perform addition and equality checks.

**Required Usage:**

* `__add__`
* `__eq__`

---

## Example – Custom Comparison for a Class

**MRP:**

Write a class representing people, and implement custom sorting based on age.

**Requirements:**

1. Use `__lt__` and `__eq__` in a `Person` class.
2. Create and sort a list of people by age.

**Required Usage:**

* `__lt__`, `__eq__`
* `sorted()`

---

## Common Pitfalls with Operators

**MRP:**

Write a script that demonstrates three common mistakes using operators and corrects them.

**Requirements:**

1. Show a comparison using `is` instead of `==`.
2. Demonstrate a mutable default argument with operator overloading.
3. Highlight an ambiguous expression without parentheses.

**Required Usage:**

* `is` vs `==`
* `__add__` or other magic methods
* Parentheses in expressions

---

## Best Practices for Operator Usage

**MRP:**

Create a guide-like script that applies best practices to example use cases involving operators.

**Requirements:**

1. Show proper use of equality and identity.
2. Use short-circuiting in conditionals.
3. Demonstrate readable formatting using parentheses.

**Required Usage:**

* `==` vs `is`
* `and`, `or`
* Parentheses in conditionals

---
