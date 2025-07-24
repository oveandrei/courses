# __init__.py

from shapes import Triangle, Circle, Square, Shapes

# Mapping shape names to their size descriptor for prompting
SHAPE_TYPES = {
    "circle": 'radius',
    "triangle": 'height',
    "square": 'size'
}

def get_valid_input(type_: str) -> str:
    """
    Prompt user for the size of the chosen shape.
    Ensures the input is a valid digit before returning it.
    """
    size = input(f"Choose a {SHAPE_TYPES[type_]} for the {type_} shape: ")
    
    # Validation loop
    while not size.isdigit():
        print(f"{SHAPE_TYPES[type_]} must be a valid number.")
        size = input(f"Choose a {SHAPE_TYPES[type_]} for the {type_} shape: ")
    
    return size


def shapes_factory(type_: str) -> Shapes:
    """
    Factory function that returns an instance of the requested shape.
    This encapsulates creation logic and isolates it from client code.

    Parameters:
    - type_: string value like 'circle', 'triangle', or 'square'

    Returns:
    - An instance of a Shapes subclass
    """
    if type_ == 'circle':
        return Circle()
    elif type_ == 'triangle':
        return Triangle()
    elif type_ == 'square':
        return Square()
    else:
        raise ValueError(f"Unknown shape type: {type_}")


def client() -> None:
    """
    Entry point for the console-based shape drawing tool.
    Allows the user to repeatedly select shapes to draw.
    """

    shapes = list(SHAPE_TYPES.keys())  # ['circle', 'triangle', 'square']
    print("Hello, this is a Factory which draws shapes of your choosing!")

    while True:
        print("\nIf you want to quit, type 'quit'.")
        type_ = input(f"Please choose a shape from the following {shapes}: ")
        type_ = type_.lower()
        
        # Input validation loop
        while type_ not in SHAPE_TYPES and type_ != 'quit':
            print("That shape is not available.")
            type_ = input(f"Please choose a shape from the following {shapes}: ")
            type_ = type_.lower()
        
        if type_ == 'quit':
            print("Exiting shape drawing tool.")
            break

        # Factory provides correct shape instance without exposing construction logic
        factory = shapes_factory(type_)
        
        # Prompt for valid size depending on shape
        size = get_valid_input(type_)
        
        # Call polymorphic draw() method
        factory.draw(int(size))


# Only run if the script is executed directly
if __name__ == "__main__":
    client()

"""
Why This is Great for Learning
Promotes OOP and abstraction clearly via Shapes.

Demonstrates separation of concerns (input handling, factory logic, shape behavior).

Uses ASCII art which is fun and visual, while being lightweight.

Makes future extension easy (just add a new class and update factory).

"""