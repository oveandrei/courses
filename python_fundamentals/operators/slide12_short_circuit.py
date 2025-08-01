def check():
    print("Function called")
    return True

# AND: stops early
print(False and check()) # Function not called -> False

# OR: stops early
print(True or check()) # Function not called -> True

# Full evaluation
print(True and check()) # Function called -> True
