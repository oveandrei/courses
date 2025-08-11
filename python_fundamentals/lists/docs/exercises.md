# A list of exercises for Python Lists

## Easy Exercises

### Creating Lists

**MRP - Minimum Requirements Product:**

Create three different lists: one from scratch, one from a string, and one using a comprehension.

**Requirements:**

1. Create an empty list.
2. Create a list from the string `"Python"`.
3. Create a list of squares for numbers 1 to 5 using a list comprehension.
4. Print all three lists.

**Required usage:**

* `list()`, `[]`, list comprehensions

---

### Accessing Elements

**MRP - Minimum Requirements Product:**

Access and display specific elements from a nested list.

**Requirements:**

1. Create a nested list with at least two inner lists.
2. Access the first element of the first inner list.
3. Access the last element of the second inner list.
4. Print both results.

**Required usage:**

* Positive indexing, negative indexing

---

### Modifying Elements

**MRP - Minimum Requirements Product:**

Update elements in a shopping list.

**Requirements:**

1. Create a list: `["apples", "bananas", "cherries"]`.
2. Replace `"bananas"` with `"oranges"`.
3. Replace the first two elements with `["grapes", "pears"]`.
4. Print the updated list.

**Required usage:**

* Index assignment, slice assignment

---

### Adding Elements

**MRP - Minimum Requirements Product:**

Add different fruits to a list using multiple methods.

**Requirements:**

1. Create a list with `["apple"]`.
2. Append `"banana"` to the list.
3. Extend the list with `["cherry", "date"]`.
4. Insert `"kiwi"` at index 1.
5. Print the final list.

**Required usage:**

* `append()`, `extend()`, `insert()`

---

### Removing Elements

**MRP - Minimum Requirements Product:**

Remove specific items from a list using different methods.

**Requirements:**

1. Create a list with `["apple", "banana", "cherry", "date"]`.
2. Remove `"banana"` using `remove()`.
3. Remove the last item using `pop()`.
4. Delete the first item using `del`.
5. Clear the list completely.
6. Print the list after each operation.

**Required usage:**

* `remove()`, `pop()`, `del`, `clear()`

---

### Slicing

**MRP - Minimum Requirements Product:**

Extract and replace parts of a list.

**Requirements:**

1. Create a list from 0 to 9.
2. Slice and print elements from index 2 to 6.
3. Slice and print every second element.
4. Reverse the list using slicing.
5. Replace the first three elements with `[100, 200, 300]`.

**Required usage:**

* Slicing syntax `[start:stop:step]`, slice assignment

---

### Searching in Lists

**MRP - Minimum Requirements Product:**

Find specific values and count occurrences.

**Requirements:**

1. Create a list with multiple `"apple"` entries.
2. Check if `"apple"` is in the list.
3. Find the index of the first `"apple"`.
4. Count how many `"apple"` entries exist.
5. Print all results.

**Required usage:**

* `in`, `index()`, `count()`

---

### Iterating Over Lists

**MRP - Minimum Requirements Product:**

Loop through names and display them with their positions.

**Requirements:**

1. Create a list of at least 4 names.
2. Use a `for` loop to print each name.
3. Use `enumerate()` to print each name with its index.

**Required usage:**

* `for` loop, `enumerate()`

---

### Copying Lists

**MRP - Minimum Requirements Product:**

Demonstrate shallow and deep copying.

**Requirements:**

1. Create a nested list: `[[1, 2], [3, 4]]`.
2. Create a shallow copy using `.copy()`.
3. Create a deep copy using `copy.deepcopy()`.
4. Modify an inner list in the shallow copy and show that it affects the original.
5. Modify an inner list in the deep copy and show that it does not affect the original.

**Required usage:**

* `copy()`, `copy.deepcopy()`

---

### Sorting & Reversing

**MRP - Minimum Requirements Product:**

Sort and reverse a list of numbers.

**Requirements:**

1. Create a list of unsorted integers.
2. Sort it in ascending order.
3. Sort it in descending order using `sorted()`.
4. Reverse the list in place.
5. Print results after each operation.

**Required usage:**

* `sort()`, `sorted()`, `reverse()`

---

### Built-in Functions with Lists

**MRP - Minimum Requirements Product:**

Apply built-in functions to a numeric list.

**Requirements:**

1. Create a list of integers.
2. Find the length, minimum, maximum, and sum.
3. Check if all numbers are positive using `all()`.
4. Check if any number is negative using `any()`.

**Required usage:**

* `len()`, `min()`, `max()`, `sum()`, `all()`, `any()`

---

### List Comprehensions

**MRP - Minimum Requirements Product:**

Create lists with comprehensions.

**Requirements:**

1. Create a list of squares for numbers 1 to 10.
2. Create a list of even numbers from 1 to 20.
3. Create a nested list (2D) using a comprehension.

**Required usage:**

* List comprehension syntax

---

### Nested Lists

**MRP - Minimum Requirements Product:**

Work with a 2D matrix.

**Requirements:**

1. Create a 3x3 matrix using a list of lists.
2. Access the element at row 2, column 3.
3. Change the value at row 1, column 1.
4. Print the updated matrix.

**Required usage:**

* Nested list indexing

---

### Memory & Mutability

**MRP - Minimum Requirements Product:**

Demonstrate that assigning a list creates a reference.

**Requirements:**

1. Create a list and assign it to another variable.
2. Modify the second variable.
3. Show that the first variable also changes.

**Required usage:**

* Variable assignment, mutability

---

### Common Pitfalls

**MRP - Minimum Requirements Product:**

Demonstrate modifying a list while iterating.

**Requirements:**

1. Create a list of numbers.
2. Remove even numbers while iterating.
3. Show that some numbers are skipped.
4. Rewrite the code to safely remove even numbers.

**Required usage:**

* `for` loop, list comprehension

---

### Lists vs Tuples vs Sets

**MRP - Minimum Requirements Product:**

Compare list, tuple, and set behavior.

**Requirements:**

1. Create a list, a tuple, and a set with duplicate values.
2. Show mutability of the list.
3. Show immutability of the tuple.
4. Show uniqueness in the set.

**Required usage:**

* `[]`, `()`, `{}`

---

### Real-World Use Cases

**MRP - Minimum Requirements Product:**

Simulate a basic inventory system.

**Requirements:**

1. Create a list representing inventory.
2. Add new items.
3. Remove sold items.
4. Display the updated inventory.

**Required usage:**

* `append()`, `remove()`

---

### Lists as Stacks (LIFO)

**MRP - Minimum Requirements Product:**

Simulate a stack.

**Requirements:**

1. Create an empty stack.
2. Push three items onto the stack.
3. Pop one item.
4. Print the stack after each operation.

**Required usage:**

* `append()`, `pop()`

---

### Lists as Queues (FIFO)

**MRP - Minimum Requirements Product:**

Simulate a queue.

**Requirements:**

1. Create an empty queue.
2. Enqueue three items.
3. Dequeue one item from the front.
4. Print the queue after each operation.

**Required usage:**

* `append()`, `pop(0)`

---

### Best Practices

**MRP - Minimum Requirements Product:**

Apply best practices to process a list.

**Requirements:**

1. Create a list of integers.
2. Generate a list of squares using a comprehension.
3. Filter out even squares without modifying the original list.
4. Use the right data structure for performance if needed.

**Required usage:**

* List comprehension, filtering, `copy()`

---

## Intermediate to Advanced exercises

### Advanced Slicing and Filtering

**MRP - Minimum Requirements Product:**

Filter and transform a list of numbers using slicing and comprehensions.

**Requirements:**

1. Create a list of numbers from 1 to 30.
2. Extract every third number starting from index 2.
3. Create a new list with only the extracted numbers that are divisible by 5.
4. Reverse the filtered list.

**Required usage:**

* Slicing `[start:stop:step]`, list comprehension, modulo operator

---

### Multi-Level Nested Access

**MRP - Minimum Requirements Product:**

Access deeply nested elements from a multi-level list.

**Requirements:**

1. Create a nested list with at least three levels of depth.
2. Access an element from the deepest level and print it.
3. Change that element’s value.
4. Print the entire structure to show the change.

**Required usage:**

* Multiple indexing, mutability

---

### Sorting with Custom Keys

**MRP - Minimum Requirements Product:**

Sort a list of tuples based on multiple criteria.

**Requirements:**

1. Create a list of tuples in the format `(name, age, score)`.
2. Sort first by age in ascending order.
3. For people with the same age, sort by score in descending order.
4. Print the sorted list.

**Required usage:**

* `sorted()`, `lambda` as key function, tuple indexing

---

### Combining and Deduplicating Lists

**MRP - Minimum Requirements Product:**

Merge multiple lists and remove duplicates while keeping order.

**Requirements:**

1. Create two lists with overlapping elements.
2. Combine them into one list.
3. Remove duplicates but preserve the original order.
4. Print the final list.

**Required usage:**

* List concatenation, loops or comprehensions, `not in`

---

### Matrix Operations

**MRP - Minimum Requirements Product:**

Perform basic operations on a 2D matrix represented as a list of lists.

**Requirements:**

1. Create a 3x3 matrix with integers from 1 to 9.
2. Extract the main diagonal as a list.
3. Transpose the matrix (rows become columns).
4. Print the transposed matrix.

**Required usage:**

* Nested list comprehension, indexing

---

### Flattening Nested Lists

**MRP - Minimum Requirements Product:**

Flatten a list of lists into a single list.

**Requirements:**

1. Create a nested list with varying inner list lengths.
2. Flatten it into a single list containing all elements.
3. Remove any duplicate values from the flattened list.

**Required usage:**

* Nested list comprehension, set conversion

---

### List as Stack with Undo Feature

**MRP - Minimum Requirements Product:**

Simulate a text editor undo feature using a list as a stack.

**Requirements:**

1. Create an empty stack.
2. Add three "actions" to the stack.
3. Undo the last action by popping from the stack.
4. Print the remaining actions.

**Required usage:**

* `append()`, `pop()`

---

### Queue Processing with Conditions

**MRP - Minimum Requirements Product:**

Simulate processing tasks from a queue until a stop condition is met.

**Requirements:**

1. Create a queue with task names, including `"STOP"` as the last task.
2. Use a while loop to dequeue and process tasks.
3. Stop processing when `"STOP"` is encountered.
4. Print each processed task.

**Required usage:**

* `append()`, `pop(0)`, `while` loop, conditional check

---

### List Transformation Pipeline

**MRP - Minimum Requirements Product:**

Apply multiple transformations to a list of numbers in a single flow.

**Requirements:**

1. Create a list of integers from 1 to 15.
2. Square all numbers.
3. Keep only those greater than 50.
4. Sort the results in descending order.
5. Print the final list.

**Required usage:**

* List comprehension, filtering, `sorted()`

---

### Detecting and Removing Outliers

**MRP - Minimum Requirements Product:**

Remove outliers from a dataset based on threshold values.

**Requirements:**

1. Create a list of integers representing sensor readings.
2. Remove any values below 10 or above 90.
3. Print the cleaned dataset.

**Required usage:**

* List comprehension, conditional filtering

---

### Chunking a List

**MRP - Minimum Requirements Product:**

Split a list into smaller chunks of a given size.

**Requirements:**

1. Create a list of integers from 1 to 20.
2. Write logic to split it into chunks of size 4.
3. Store the chunks in a new list of lists.
4. Print the result.

**Required usage:**

* Slicing, loops or comprehension

---

### Generating a Multiplication Table

**MRP - Minimum Requirements Product:**

Generate a multiplication table stored as a nested list.

**Requirements:**

1. Create a nested list where the value at `[i][j]` is `(i+1) * (j+1)`.
2. Use 5 rows and 5 columns.
3. Print the table.

**Required usage:**

* Nested list comprehension

---
