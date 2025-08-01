value = None
x, y = 5, 10

# Clear equality vs identity check
if value == None:  # AVOID
    pass

if value is None: # PREFERRED
    pass

# Parentheses for clarity
if (x > 0 and x < 10) or y == 5:
    print("In range or y equals 5")