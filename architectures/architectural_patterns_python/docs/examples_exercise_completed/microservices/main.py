from user_service import service as user_service
from product_service import service as product_service
from order_service import service as order_service
from order_service.models import Cart
from handlers import main_menu, handle_order_service, handle_product_service, handle_user_service

def main():
    """
    Entry point for the CLI-based e-commerce platform.

    This function controls the main loop that displays the main menu and routes user
    selections to the appropriate service handlers (User, Product, Order).

    It maintains the current logged-in user state to pass it to relevant handlers.

    The loop continues until the user chooses to quit.
    """
    current_user: str | None = None  # Tracks currently logged-in username or None if no user logged in

    while True:
        choice = main_menu()  # Display main menu and get user choice

        if choice == "1":
            # Handle user-related operations such as register, login, view profile, logout
            current_user = handle_user_service(current_user)

        elif choice == "2":
            # Handle product-related operations like listing, adding, updating products
            handle_product_service()

        elif choice == "3":
            # Handle order-related operations like managing cart and placing orders
            handle_order_service(current_user)

        elif choice == "4":
            # Exit the application
            print("Goodbye!")
            break

        else:
            # Invalid input, prompt user again
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Run main() only if this script is executed directly
    main()
