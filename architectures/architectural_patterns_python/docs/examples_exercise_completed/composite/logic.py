from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    """
    Abstract base class for all file system components (files and folders).
    Enforces implementation of display() and get_size() methods.
    """

    @abstractmethod
    def display(self, indent: int = 0) -> None:
        """Display the structure of the component with optional indentation."""
        pass

    @abstractmethod
    def get_size(self) -> int:
        """Return the size of the component (files return their size, folders return total size of contents)."""
        pass


class Folder(FileSystemComponent):
    """
    Represents a folder which can contain other files or folders.
    Implements the Composite pattern by managing a collection of child FileSystemComponents.
    """

    def __init__(self, name: str) -> None:
        self.name = name  # Name of the folder
        self._children: list[FileSystemComponent] = []  # List of child components (files or folders)

    def add(self, item: FileSystemComponent) -> None:
        """
        Adds a File or Folder to the folder's children.
        """
        self._children.append(item)

    def display(self, indent: int = 0) -> None:
        """
        Recursively displays the folder and its contents using indentation.
        """
        print("  " * indent + f"Folder: {self.name}")
        for child in self._children:
            child.display(indent + 1)

    def get_size(self) -> int:
        """
        Recursively calculates the total size of all contents in the folder.
        """
        return sum(child.get_size() for child in self._children)


class File(FileSystemComponent):
    """
    Represents a file with a fixed size.
    Acts as a leaf node in the Composite pattern.
    """

    def __init__(self, name: str, size: int) -> None:
        self.name = name  # File name
        self.size = size  # File size

    def display(self, indent: int = 0) -> None:
        """
        Displays the file name with indentation based on depth in folder structure.
        """
        print("  " * indent + f"File: {self.name}")

    def get_size(self) -> int:
        """
        Returns the file's size.
        """
        return self.size


class FileManager:
    """
    Manages all file objects in the system, preventing duplicate names and providing access.
    """
    files_dict: dict[str, File] = {}  # Registry of all created files

    def get_file_object(self, name: str) -> File:
        """
        Returns the File object associated with the given name.
        Raises KeyError if file does not exist.
        """
        return self.files_dict[name]

    def file_add_dict(self, name: str, file_object: File) -> None:
        """
        Adds a file to the registry.
        """
        self.files_dict[name] = file_object

    def get_all_files(self) -> list[str]:
        """
        Returns a list of all registered file names.
        """
        return list(self.files_dict.keys())

    def create_and_register_file(self, name: str, size: int) -> File | None:
        """
        Creates a new file and registers it.
        Returns the File object if successful, or None if a file with the same name already exists.
        """
        if name in self.files_dict:
            return None
        new_file = File(name, size)
        self.file_add_dict(name, new_file)
        return new_file


class FolderManager:
    """
    Manages all folder objects in the system, preventing duplicates and allowing lookup.
    """
    folders_dict: dict[str, Folder] = {}  # Registry of all created folders

    def get_folder_object(self, name: str) -> Folder:
        """
        Returns the Folder object associated with the given name.
        Raises KeyError if folder does not exist.
        """
        return self.folders_dict[name]

    def folder_add_dict(self, name: str, folder_object: Folder) -> None:
        """
        Adds a folder to the registry.
        """
        self.folders_dict[name] = folder_object

    def get_all_folders(self) -> list[str]:
        """
        Returns a list of all registered folder names.
        """
        return list(self.folders_dict.keys())

    def create_and_register_folder(self, name: str) -> Folder | None:
        """
        Creates a new folder and registers it.
        Returns the Folder object if successful, or None if a folder with the same name already exists.
        """
        if name in self.folders_dict:
            return None
        new_folder = Folder(name)
        self.folder_add_dict(name, new_folder)
        return new_folder
