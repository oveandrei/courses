from theme import Theme
from language import Language
from singleton import SingletonMeta

class Config(metaclass=SingletonMeta):
    def __init__(self):
        self.language = Language() # We initialize the Language class containing the languages
        self.theme = Theme() # We initialize the Theme class containing the themes
    
    def read_values(self):
        """
        We implement the settings dictionary in a function so we can dynamically check any changes that have been made
        And to not be forced to update manually the settings whenever the user changes a setting.
        """
        settings: dict = {
            'language': self.language._language,
            'theme': self.theme._theme,
        }
        return settings 

    def __call__(self): # We use the __call__ so we can treat the class as a function
        ongoing = True # Placehorder for the loop <- you can also not use this and just use a while True with a break block
        print("Hello! This is your Setting Manager App!") # Only once this should be shown
        while ongoing:
            # List with options you have in the app
            print("What would you like to do?")
            print("------------------------")
            print('1: View your current settings')
            print('2: Change theme settings')
            print('3: Change Language settings')
            print('4: quit')
            print('--------------------------')
            response = input("Please choose a number:") # We get the number input of the user

            # We check the number
            if response == '1':
                print("Your current settings are:")
                print(self.read_values()) # We dynamically get the current settings
                print('----------------------------')
            elif response == '2':
                self.theme() # We take advantage of the __call__ method in theme and language
            elif response == '3':
                self.language()
            elif response == '4':
                print("Quitting the application...")
                ongoing = False # We stop the loop
            else:
                print("Your answer is not a correct answer.... Please choose a valid number")

if __name__ == "__main__":
    # Instantiate the class multiple times
    c1 = Config()
    c2 = Config()

    # Check if both instances are actually the same object
    print(c1 is c2)  # Output: True — proves Singleton behavior

    # Check for the initial settings
    print(c1.read_values())

    # Initialize the __call__ in Config
    c1()

    # Check for final settings
    print(c1.read_values())