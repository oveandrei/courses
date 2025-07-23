# help(): get docs for any object
help(str)                       # Shows all string methods and docstrings
help(len)                       # Shows the function's purpose and usage

# __import__(): dynamically import modules by name
mod_name = "math"
math_mod = __import__(mod_name)
print(math_mod.sqrt(16))        # Output: 4.0

# Dynamic import is useful in plugins, CLI tools, etc.
