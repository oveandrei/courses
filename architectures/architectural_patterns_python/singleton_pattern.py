# Define a metaclass that controls the instantiation process
class SingletonMeta(type):
    _instance = None  # This will store the single instance of the class

    def __call__(cls, *args, **kwargs):
        # __call__ is triggered when you instantiate a class
        if cls._instance is None:
            # If no instance exists, create one
            cls._instance = super().__call__(*args, **kwargs)
        # Return the same instance every time
        return cls._instance

# Apply the SingletonMeta metaclass to your class
class Config(metaclass=SingletonMeta):
    def __init__(self):
        # You can initialize configuration values or any shared state here
        self.settings = {
            "db": "localhost",
            "port": 5432
        }

# Instantiate the class multiple times
c1 = Config()
c2 = Config()

# Check if both instances are actually the same object
print(c1 is c2)  # Output: True — proves Singleton behavior

# You can access the same shared state from both variables
print(c1.settings)  # {'db': 'localhost', 'port': 5432'}
print(c2.settings)  # {'db': 'localhost', 'port': 5432'}
