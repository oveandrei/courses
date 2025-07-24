'''datetime'''

from datetime import date, datetime, time, timedelta

# Current date and time
now = datetime.now()
print(now)

# Create a specific date
d = date(2025, 12, 15)
print(d) # 2025-12-15

# Create a speficific time
t = time(14, 30)
print(t) # 14:30:00

# Combine date and time
combined = datetime.combine(d, t)
print(combined) # 2025-12-15 14:30:00

# Add 5 days
future = now + timedelta(days=5)
print(future) # e.g., 2025-07-29

# Format datetime as string
formatted = now.strftime("%Y-%m-%d %H:%M")
print(formatted) 

# Parse string into datetime
parsed = datetime.strptime("2025-07-24 14:32", "%Y-%m-%d %H-%M")
print(parsed)


'''timeit'''

import timeit

# Example 1: Time a single line of code
time_taken = timeit.timeit('"-".join(str(n)) for n in range(100)', number=1000)
print(time_taken)

# Example 2: Using a setup block and multi-line code
setup_code = "from math import sqrt"
code_to_test = """
def compute():
    return [sqrt(x) for x in range(100)]
compute()
"""
execution_time = timeit.timeit(code_to_test, setup=setup_code, number=1000)
print(execution_time) # e.g., 0.15 seconds

# Example 3: Using Timer class
from timeit import Timer

t = Timer("sum(range(100))")
print(t.timeit(number=1000)) # Similar to above