from base import GUIFactory
from windows import WindowsFactory
from linux import LinuxFactory

def select_factory() -> dict:
    """
    Returns a dictionary mapping OS names to their corresponding GUI factories.

    This allows the client to dynamically choose the appropriate GUI factory
    at runtime without hardcoding platform-specific logic.
    """
    component = {
        'windows': WindowsFactory(),
        'linux': LinuxFactory()
    }
    return component

def create_ui(factory: GUIFactory) -> None:
    """
    Creates UI components (button and checkbox) using the given factory,
    and renders them.

    Args:
        factory (GUIFactory): A factory object that creates platform-specific UI components.
    """
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.render()
    checkbox.render()

def client() -> None:
    """
    Main client loop that allows the user to select an OS
    and renders the corresponding UI using the Abstract Factory pattern.

    The loop continues until the user enters 'quit'.
    """
    print("This is your Cross-Platform UI Kit.")
    while True:
        print("If you want to quit, type 'quit'.")
        response = input(f"Please choose the operating system you want to use: Windows or Linux: ")
        response = response.lower()

        factories = select_factory()  # Get available factories
        
        if response == 'quit':
            break

        if response not in factories:
            print("That operating system is not available.")
        else:
            create_ui(factories[response])

# Entry point
if __name__ == "__main__":
    client()
