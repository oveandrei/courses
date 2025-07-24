"""
This class will act as the singleton pattern to all classes in this exercise to ensure both the system and the subsystems are treated as singleton
"""

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
    
