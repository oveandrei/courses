'''unittest'''
import unittest

# Funtion to test
def add(a, b):
    return a + b

# Test case
class TestMatch(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

# Run tests if this file is executed
if __name__ == "__main__":
    unittest.main()
# Run with python test_file.py or python -m unittest tests.py


'''doctest'''
def multiply(x, y):
    """
    Multiplies two numbers.

    >>> multiply(2, 3)
    6    
    >>> multiplay(-1, 5)
    -5
    """
    return x * y

if __name__ == "__main__":
    import doctest
    doctest.testmod()
# Automatically checks that the docstring examples run and return expected values


'''trace'''
import trace

# Trace execution of a script
tracer = trace.Trace(trace=True, count=False)
tracer.run('print("Tracing this line")')
# Outputs each line of code as it executes - useful for debugging flow.


'''pdb'''
import pdb

def calculate():
    a = 10
    b = 5
    pdb.set_trace() # Enter interactive debugging
    c = a + b
    print(c)

calculate()
# When the debugger pauses, you can type commands


'''inspect'''
import inspect

def greet(name: str) -> str:
    """Greets the user"""
    return f"Hello, {name}"

# Get function signature
print(inspect.signature(greet)) # (name: str) -> str

# Get source code
print(inspect.getsource(greet))
# Helps with dynamic introspection, decorators and debugging.


'''traceback'''
import traceback

try:
    1 / 0 # type: ignore
except Exception as e:
    print("Error captured:")
    traceback.print_exc()
# Outputs the full stack trace - often used in loggin for detailed crash reports.


'''cProfile, profile, pstats'''
import cProfile

def run():
    total = 0
    for i in range(1000):
        total += i ** 2
    return total

cProfile.run('run()')

import pstats

# Load and analyze a saved profile
stats = pstats.Stats('profile_output.prof')
stats.sort_stats('time').print_stats(10)
# Use cProfile.run('run()', 'profile_output.prof') to save profile data.