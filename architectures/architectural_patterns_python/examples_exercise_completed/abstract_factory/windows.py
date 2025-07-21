from base import Button, Checkbox, GUIFactory

# Concrete implementation of a Windows-styled button
class WindowsButton(Button):
    def render(self) -> None:
        print("Render a Windows-style button.")

# Concrete implementation of a Windows-styled checkbox
class WindowsCheckbox(Checkbox):
    def render(self) -> None:
        print("Render a Windows-style checkbox.")

# Concrete factory for creating Windows UI components
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        """
        Returns a Windows-specific button.
        """
        return WindowsButton()
    
    def create_checkbox(self) -> Checkbox:
        """
        Returns a Windows-specific checkbox.
        """
        return WindowsCheckbox()
