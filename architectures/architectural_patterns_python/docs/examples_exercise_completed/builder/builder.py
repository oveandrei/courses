from components import COMPONENTS
from dataclasses import dataclass

@dataclass(frozen=True)
class PC:
    """
    Immutable PC configuration object built using the PCBuilder.

    Attributes:
        cpu (str): The CPU model.
        ram (str): The RAM size and type.
        gpu (str): The GPU model.
        storage (str): The storage type and size.
    """
    cpu: str
    ram: str
    gpu: str
    storage: str


class PCBuilder:
    """
    Builder class for constructing a custom PC configuration step-by-step.

    Methods:
        set_cpu(cpu): Sets the CPU.
        set_ram(ram): Sets the RAM.
        set_gpu(gpu): Sets the GPU.
        set_storage(storage): Sets the storage.
        build(): Validates and builds the final immutable PC object.
    """

    def __init__(self):
        """
        Initializes the builder with empty component values.
        All components must be set before building.
        """
        self._cpu = None
        self._ram = None
        self._storage = None
        self._gpu = None

    def set_cpu(self, cpu: str) -> 'PCBuilder':
        """
        Sets the CPU for the PC.

        Args:
            cpu (str): The CPU model.

        Returns:
            PCBuilder: The builder instance for method chaining.
        """
        self._cpu = cpu
        return self

    def set_ram(self, ram: str) -> 'PCBuilder':
        """
        Sets the RAM for the PC.

        Args:
            ram (str): The RAM size and type.

        Returns:
            PCBuilder: The builder instance for method chaining.
        """
        self._ram = ram
        return self

    def set_gpu(self, gpu: str) -> 'PCBuilder':
        """
        Sets the GPU for the PC.

        Args:
            gpu (str): The GPU model.

        Returns:
            PCBuilder: The builder instance for method chaining.
        """
        self._gpu = gpu
        return self

    def set_storage(self, storage: str) -> 'PCBuilder':
        """
        Sets the storage for the PC.

        Args:
            storage (str): The storage type and size.

        Returns:
            PCBuilder: The builder instance for method chaining.
        """
        self._storage = storage
        return self

    def build(self) -> PC:
        """
        Builds the final PC object after validating that all components are set.

        Returns:
            PC: The fully constructed immutable PC object.

        Raises:
            ValueError: If any required component is missing.
        """
        if not all([self._cpu, self._ram, self._gpu, self._storage]):
            raise ValueError("All components must be set before building the PC.")
        # Don't mind the error.
        return PC(cpu=self._cpu, ram=self._ram, gpu=self._gpu, storage=self._storage) # type: ignore
