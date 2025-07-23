
'''eval() vs exec()'''
x = 10

# eval() evaluates a string as a Python *expression*
# Safe here because we're controlling the input
print(eval("x + 5"))     # Output: 15

# exec() executes a string as a block of Python *code*
# It can include assignments, loops, function defs, etc.
exec("y = x * 2")        # Defines y in the current scope
print(y)                  # Output: 20 # type: ignore

'''compile()'''
# compile() can convert source code into a code object
# Use mode='eval' for expressions (can also use 'exec' or 'single')
code = "x + 3"

compiled = compile(code, "<string>", "eval")  # Filename is optional label
print(eval(compiled))    # Output: 13 — safely evaluates the precompiled code
