
# Existing class with an incompatible interface
class OldPrinter:
    def old_print(self, text: str) -> None:
        print(f"[OldPrinter] {text}")

# New interface expected by the system
class Printer:
    def prnt(self, text: str) -> None:
        raise NotImplementedError

# Adapter that makes OldPrinter compatible with Printer
class PrinterAdapter(Printer):
    def __init__(self, adaptee: OldPrinter):
        self._adaptee = adaptee

    def prnt(self, text: str) -> None:
        # Translate the call from the new interface to the old one
        self._adaptee.old_print(text)

# Client code that works with the new interface
def client_code(printer: Printer):
    printer.prnt("Hello from the new system!")

# Example usage
legacy_printer = OldPrinter()
adapter = PrinterAdapter(legacy_printer)
client_code(adapter) # Internally calls old_print()