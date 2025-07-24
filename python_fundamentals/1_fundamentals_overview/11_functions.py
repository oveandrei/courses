
'''How to define a function in Python'''
def function_name(parameter: str) -> str: # We say parameter must be a str and the function has to return a str, you are not forced to do this but its good to do it always
    # block of code
    return parameter # optional
function_name('example') # calling the function.
# To be noted that we have to encapsulate the function call in a variable or print() to see the result from the 'return`


'''Lambda Function'''
lambda_function = lambda x: x*2 # this is a simple lambda function that doubles the input


'''Function with default parameters'''
def greet(name: str = "World") -> str: # in this example name has the default value of 'World" if nothing is passed for the parameter.
    return f"Hello, {name}"


'''Function with multiple parameters'''
def add_numbers(a: int, b: int) -> int:
    return a + b


'''Adding descriptive docstring to the functions'''
def function_with_docstring(param1: int, param2: int) -> int:
    """
    This function adds two integers and returns the result.

    Args:
        param1 (int): The first integer to add.
        param2 (int): The second integer to add.
    
    Returns:
        int: The sum of the two integers.
    """
    return param1 + param2


'''Testing the functions'''
print(greet()) # Output: Hello, World