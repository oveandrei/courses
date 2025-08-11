stack = []
stack.append("A")  # Push: Add 'A' to the top of the stack
stack.append("B")  # Push: Add 'B' on top of 'A'
print(stack)       # Output: ['A', 'B']

print(stack.pop()) # Pop: Removes and returns 'B' (last in)
print(stack)       # Output: ['A']
