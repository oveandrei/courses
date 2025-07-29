def prompt_nonempty(prompt: str) -> str:
    """
    Prompt the user repeatedly until a non-empty string is entered.

    Args:
        prompt (str): The text to display to the user.

    Returns:
        str: The non-empty user input.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def prompt_int_nonnegative(prompt: str) -> int:
    """
    Prompt the user repeatedly until a valid non-negative integer is entered.

    Args:
        prompt (str): The text to display to the user.

    Returns:
        int: The non-negative integer entered by the user.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
            if value < 0:
                # Reject negative integers
                raise ValueError
            return value
        except ValueError:
            print("Please enter a non-negative integer.")


def prompt_float_positive(prompt: str) -> float:
    """
    Prompt the user repeatedly until a valid positive float is entered.

    Args:
        prompt (str): The text to display to the user.

    Returns:
        float: The positive float entered by the user.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value <= 0:
                # Reject zero or negative floats
                raise ValueError
            return value
        except ValueError:
            print("Please enter a positive number.")


def print_products_table(rows: list[dict]) -> None:
    """
    Pretty-print a list of product dictionaries as a formatted table.

    Each dictionary in `rows` must have keys: "id", "name", "price", "stock".

    Args:
        rows (list[dict]): List of product data dictionaries.
    """
    if not rows:
        print("No products found.")
        return

    # Calculate column widths based on longest values or minimum widths
    id_w = max(10, max(len(str(r["id"])) for r in rows))
    name_w = max(12, max(len(str(r["name"])) for r in rows))
    price_w = 10  # Fixed width for price column
    stock_w = 7   # Fixed width for stock column

    # Prepare header and separator lines
    header = f'{"ID":<{id_w}}  {"Name":<{name_w}}  {"Price":>{price_w}}  {"Stock":>{stock_w}}'
    sep = "-" * len(header)
    print(header)
    print(sep)

    # Print each product row formatted by column widths
    for r in rows:
        print(f'{str(r["id"]):<{id_w}}  {str(r["name"]):<{name_w}}  {r["price"]:>{price_w}.2f}  {r["stock"]:>{stock_w}d}')
