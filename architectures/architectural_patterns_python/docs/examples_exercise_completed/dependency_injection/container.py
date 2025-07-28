from typing import Any, Callable

class Container:
    """
    A simple dependency injection (DI) container.

    Allows registering and resolving services using factory functions.
    Supports lazy instantiation (new object each time).
    """

    def __init__(self):
        """
        Initialize an empty container with no registered dependencies.
        """
        self._dependencies: dict[str, Callable[[], Any]] = {}

    def register(self, name: str, constructor: Callable[[], Any]) -> None:
        """
        Register a dependency with a given name and a factory function.

        Args:
            name (str): The unique key to register the service under.
            constructor (Callable[[], Any]): A factory function that returns a new instance of the dependency.
        """
        self._dependencies[name] = constructor

    def resolve(self, name: str) -> Any:
        """
        Resolve a registered dependency by name, calling its factory function.

        Args:
            name (str): The name of the registered dependency.

        Returns:
            Any: A new instance of the resolved dependency.

        Raises:
            ValueError: If the name is not registered in the container.
        """
        if name not in self._dependencies:
            raise ValueError(f"No provider registered for '{name}'")
        return self._dependencies[name]()
