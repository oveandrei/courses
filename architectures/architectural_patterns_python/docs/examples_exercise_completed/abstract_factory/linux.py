from base import Button, Checkbox, GUIFactory

# Concrete implementation of a Linux-styled button
class LinuxButton(Button):
    def render(self) -> None:
        print("Render a Linux-style Button.")

# Concrete implementation of a Linux-styled checkbox
class LinuxCheckbox(Checkbox):
    def render(self) -> None:
        print("Render a Linux-style checkbox.")

# Concrete factory for creating Linux UI components
class LinuxFactory(GUIFactory):
    def create_button(self) -> Button:
        """
        Returns a Linux-specific button.
        """
        return LinuxButton()
    
    def create_checkbox(self) -> Checkbox:
        """
        Returns a Linux-specific checkbox.
        """
        return LinuxCheckbox()
