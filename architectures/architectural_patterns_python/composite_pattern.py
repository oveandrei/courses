from abc import ABC, abstractmethod

# Base component class
class FileSystemItem(ABC):
    @abstractmethod
    def show(self, indent: int = 0) -> None:
        """Display the item with indentation base on hierarchy level."""
        pass

# Leaf class - cannot contain other items
class File(FileSystemItem):
    def __init__(self, name: str):
        self.name = name

    def show(self, indent: int = 0) -> None:
        print("  " * indent + f"File: {self.name}")

# Composit class - can contain children
class Folder(FileSystemItem):
    def __init__(self, name: str):
        self.name = name
        self._children: list[FileSystemItem] = []

    def add(self, item: FileSystemItem) -> None:
        """Add a file or folder to this folder."""
        self._children.append(item)
    
    def show(self, indent: int = 0) -> None:
        print("  " * indent + f"Folder: {self.name}")
        for child in self._children:
            child.show(indent + 1) # Recursively show children with more indentation

# Usage
root = Folder("root")
root.add(File("file1.txt"))
root.add(File("file2.txt"))

sub_folder = Folder("subfolder")
sub_folder.add(File("nested_file.txt"))

root.add(sub_folder)

# Display the whole file structure
root.show()