"""
A module where we implement the logic of the Language class.
In order to not duplicate comments and considering language and theme classes are duplicated
With the same logic
Please check theme.py comments"""

from singleton import SingletonMeta




class Language(metaclass=SingletonMeta):
    def __init__(self):
        self._language: str = 'english'
        self._language_options: list = ['english', 'french', 'romanian', 'spanish']

    def __call__(self):
        response = input(f"The current language: {self._language}. Please choose a new language from the following {self._language_options}:")
        response = response.lower()
        while response not in self._language_options:
            print("That language is not available.")
            response = input(f"The current language: {self._language}. Please choose a new language from the following {self._language_options}:")
    
        self._language = response
        print(f"Language set to {self._language}")
        return self._language

