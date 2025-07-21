from singleton import SingletonMeta
"""A module where we implement the logic of the Theme class."""


class Theme(metaclass=SingletonMeta):
    def __init__(self):
        self._theme: str = 'white' # We set a default theme to white
        self._themes: list = ['black', 'white', 'grey'] # We give the users a list of themes from which they can choose on
    
    def __call__(self): # We do __call__ so we can treat the class a function directly
        response = input(f"The current theme: {self._theme}. Please choose a new theme from the following {self._themes}:")
        response = response.lower() # We ensure the input of the user is treated as lowercase beause our list contains only lowercase
        while response not in self._themes: # We loop this lines until user gives a valid input
            print("That theme is not available.")
            response = input(f"The current theme: {self._theme}. Please choose a new theme from the following {self._themes}:")
            
            
        self._theme = response # finally we set the new theme to a correct response
        print(f"Theme set to {self._theme}")
        return self._theme # We return the new theme

