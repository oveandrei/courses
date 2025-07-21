from builder import PCBuilder
from components import COMPONENTS

def validate(component: str, type_: str) -> str:
    """
    Validates that the user's selected component exists in the predefined COMPONENTS.

    Args:
        component (str): The component type (CPU, GPU, RAM, STORAGE).
        type_ (str): The user's selected value.

    Returns:
        str: A valid, confirmed component string in uppercase.
    """
    type_ = type_.upper()

    while type_ not in COMPONENTS[component]:
        print("-------------------------------------------------------------")
        print(f"The component {type_} doesn't exist in our list of {component}")
        print(f"List of {component}: {COMPONENTS[component]}")
        type_ = input(f"Choose a {component} from the list above: ")
        type_ = type_.upper()

    return type_

def client_cli():
    """
    CLI interface to build a custom PC using the PCBuilder.

    Prompts the user for each component, validates input, and constructs the PC.
    
    Returns:
        PC: The fully constructed and immutable PC object if successful.
    """
    cpu = gpu = ram = storage = None
    builder = PCBuilder()

    print('This is your PC Builder APP.')
    for component in COMPONENTS:
        print("---------------------------------------------------------")
        print(f"List of {component}: {COMPONENTS[component]}")
        response = input(f"Choose a {component} from the list above: ")
        response = response.upper()
        response = validate(component, response)

        if component == 'CPU':
            cpu = response
        elif component == 'GPU':
            gpu = response
        elif component == "RAM":
            ram = response
        elif component == 'STORAGE':
            storage = response

    if cpu and gpu and ram and storage:
        pc = builder.set_cpu(cpu).set_gpu(gpu).set_ram(ram).set_storage(storage).build()
        return pc

if __name__ == '__main__':
    print(client_cli())
