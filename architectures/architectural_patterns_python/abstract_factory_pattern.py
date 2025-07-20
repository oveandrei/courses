from abc import ABC, abstractmethod

# Abstract products
class Button(ABC):
    @abstractmethod
    def render(self) -> None:
        """Render the button on the screen."""
        pass

class Checkbox(ABC):
    @abstractmethod
    def check(self) -> None:
        """Check or uncheck the checkbox."""
        pass

# Concrete products - Windows style
class WindowsButton(Button):
    def render(self) -> None:
        print("Render a Windows-syle button.")

class WindowsCheckbox(Checkbox):
    def check(self) -> None:
        print("Check a Windows-style Checkbox.")

# Concrete products - macOS style
class MacButton(Button):
    def render(self) -> None:
        print("Render a Mac-style button.")

class MacCheckbox(Checkbox):
    def check(self) -> None:
        print("Check a Mac-style Checkbox")

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete factories
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Client code - works with any factory
def create_ui(factory: GUIFactory) -> None:
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.render() # Renders platform specific button
    checkbox.check() # Checks platform-specific checkbox

# Usage
factory =  WindowsFactory()
create_ui(factory)
factory = MacFactory()
create_ui(factory)
    