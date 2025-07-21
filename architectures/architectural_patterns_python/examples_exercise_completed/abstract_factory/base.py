from abc import ABC, abstractmethod

# Abstract base class for all buttons
class Button(ABC):
    @abstractmethod
    def render(self) -> None:
        """
        Render the button on the screen.
        Must be implemented by subclasses.
        """
        pass

# Abstract base class for all checkboxes
class Checkbox(ABC):
    @abstractmethod
    def render(self) -> None:
        """
        Render a checkbox on the screen.
        Must be implemented by subclasses.
        """
        pass

# Abstract Factory for creating UI components
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        """
        All subclasses must implement a method to create a button.
        """
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        """
        All subclasses must implement a method to create a checkbox.
        """
        pass
