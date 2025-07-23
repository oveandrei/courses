# repr() gives detailed string (good for debugging)
text = "hello\nworld"
print(repr(text))             # 'hello\nworld'

# ascii() escapes non-ASCII safely
emoji = "café ☕"
print(ascii(emoji))           # 'caf\\xe9 \\u2615'

# format() with float precision
pi = 3.14159265
print(format(pi, ".2f"))      # '3.14'

# format() for padding and alignment
n = 42
print(format(n, "04"))        # '0042'
print(format(n, "<6"))        # '42    '

# Also works with named placeholders
template = "Name: {name}, Age: {age}"
print(template.format(name="Ada", age=30))  # 'Name: Ada, Age: 30'
