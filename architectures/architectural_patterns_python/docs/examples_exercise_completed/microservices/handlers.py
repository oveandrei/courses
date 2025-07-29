from order_service import service as order_service
from product_service import service as product_service
from user_service import service as user_service
from order_service.models import Cart
from helpers import prompt_nonempty, prompt_int_nonnegative, prompt_float_positive, print_products_table

# Initialize a single shared cart instance for all users
cart = Cart()


def main_menu() -> str:
    """
    Display the main menu of the e-commerce platform.

    Returns:
        str: The user's menu choice as a string.
    """
    print("\n--- E-Commerce Platform ---")
    print("1. User Service")
    print("2. Product Service")
    print("3. Order Service")
    print("4. Quit")
    return input("Choose a service: ").strip()


def user_menu() -> str:
    """
    Display the user service submenu.

    Returns:
        str: The user's choice for user service actions.
    """
    print("\n--- User Service ---")
    print("1. Register User")
    print("2. Log In")
    print("3. View Profile")
    print("4. Log out")
    print("5. Back to Main Menu")
    return input("Choose an option: ").strip()


def product_menu() -> str:
    """
    Display the product service submenu.

    Returns:
        str: The user's choice for product service actions.
    """
    print("\n--- Product Service ---")
    print("1. List All Products")
    print("2. Add Product")
    print("3. Search Product by Name")
    print("4. Update Stock")
    print("5. Update Price")
    print("6. Rename Product")
    print("7. Delete Product")
    print("8. Back to Main Menu")
    return input("Choose an option: ").strip()


def order_menu() -> str:
    """
    Display the order service submenu.

    Returns:
        str: The user's choice for order service actions.
    """
    print("\n--- Order Service ---")
    print("1. Add to Cart")
    print("2. View My Cart")
    print("3. Place Order")
    print("4. View My Orders")
    print("5. Back to Main Menu")
    return input("Choose an option: ").strip()


def handle_user_service(current_user: str | None) -> str | None:
    """
    Handle user service operations including registration, login,
    viewing profile, and logout.

    Args:
        current_user (str | None): Username of currently logged-in user, or None.

    Returns:
        str | None: Updated current user after operations.
    """
    while True:
        choice = user_menu()

        if choice == "1":
            username = prompt_nonempty("Enter username: ")
            password = prompt_nonempty("Enter password: ")
            user_service.register_user(username, password)

        elif choice == "2":
            username = prompt_nonempty("Enter username: ")
            password = prompt_nonempty("Enter password: ")
            current_user = user_service.login(username, password)

        elif choice == "3":
            if current_user:
                user_service.view_profile(current_user)
            else:
                print("Please log in first.")

        elif choice == "4":
            # Try to logout using user_service; fallback if not implemented
            try:
                current_user = user_service.logout(current_user)
            except AttributeError:
                if current_user:
                    print(f"Logged out '{current_user}'.")
                current_user = None

        elif choice == "5":
            # Back to main menu, return current user state
            return current_user
        else:
            print("Invalid option.")


def handle_product_service() -> None:
    """
    Handle product service operations including listing, adding,
    searching, updating, renaming, and deleting products.
    """
    while True:
        choice = product_menu()

        if choice == "1":
            rows = product_service.list_all_products()
            print_products_table(rows)

        elif choice == "2":
            name = prompt_nonempty("Product name: ")
            price = prompt_float_positive("Price: ")
            stock = prompt_int_nonnegative("Initial stock: ")
            product_service.add_product(name, price, stock)

        elif choice == "3":
            name = prompt_nonempty("Exact product name to search: ")
            prod = product_service.search_product_by_name(name)
            if prod:
                print(f"Found: {prod.product_id} | {prod.name} | {prod.price:.2f} | Stock: {prod.stock}")
            else:
                print("No exact match found.")

        elif choice == "4":
            name = prompt_nonempty("Exact product name to update stock: ")
            new_stock = prompt_int_nonnegative("New stock value: ")
            product_service.update_stock(name, new_stock)

        elif choice == "5":
            name = prompt_nonempty("Exact product name to update price: ")
            new_price = prompt_float_positive("New price: ")
            product_service.update_price(name, new_price)

        elif choice == "6":
            name = prompt_nonempty("Exact current product name: ")
            new_name = prompt_nonempty("New product name: ")
            product_service.update_name(name, new_name)

        elif choice == "7":
            name = prompt_nonempty("Exact product name to delete: ")
            product_service.delete_product(name)

        elif choice == "8":
            # Back to main menu
            return
        else:
            print("Invalid option.")


def handle_order_service(current_user: str | None) -> None:
    """
    Handle order service operations including adding to cart,
    viewing cart, placing orders, and viewing user's orders.

    Args:
        current_user (str | None): Username of currently logged-in user.

    Returns:
        None
    """
    if not current_user:
        print("Please log in to use Order Service.")
        return

    while True:
        choice = order_menu()

        if choice == "1":
            name = prompt_nonempty("Product name: ")
            quantity = prompt_int_nonnegative("Quantity: ")
            cart.add_to_cart(current_user, name, quantity)
            print(f"Added {quantity} x {name} to your cart.")

        elif choice == "2":
            items = cart.get_cart(current_user)
            if not items:
                print("Your cart is empty.")
            else:
                print("\nYour Cart:")
                for item in items:
                    print(f"- {item.product_name} (x{item.quantity})")

        elif choice == "3":
            order = order_service.place_order(current_user, cart)
            if order:
                print(f"✅ Order placed! Order ID: {order.order_id}")
            else:
                print("❌ Could not place order (maybe your cart is empty).")

        elif choice == "4":
            orders = order_service.load_orders()
            found = [o for o in orders.values() if o.user_username == current_user]
            if not found:
                print("You have no orders.")
            else:
                print("\nYour Orders:")
                for o in found:
                    print(f"🧾 ID: {o.order_id} | Status: {o.status}")
                    for item in o.items:
                        print(f"   - {item.product_name} x{item.quantity}")

        elif choice == "5":
            # Back to main menu
            return

        else:
            print("Invalid option.")
