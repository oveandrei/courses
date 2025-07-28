from container import Container
from notification_service import UserRegistrationService
from providers import SMSSender, EmailSender, PushSender

def main_menu() -> None:
    """
    Display the main menu options to the user.
    """
    print("\n--- Main Menu ---")
    print("1. Register user")
    print("2. Quit")

def choose_channel() -> str:
    """
    Prompt the user to choose a notification channel.

    Returns:
        str: The chosen channel key ('SMS', 'EMAIL', or 'PUSH').
             Defaults to 'SMS' if input is invalid.
    """
    print("\nChoose Notification Channel:")
    print("1. SMS")
    print("2. Email")
    print("3. Push")
    choice = input("Enter choice: ")
    mapping = {'1': 'SMS', '2': 'EMAIL', '3': 'PUSH'}
    return mapping.get(choice, 'SMS')  # Default to SMS if invalid

def main() -> None:
    """
    Entry point of the application.

    Sets up the DI container, registers notification providers,
    and handles the main user interaction loop for registration.
    """
    # Set up DI container
    container = Container()

    # Register providers with factories
    container.register("SMS", lambda: SMSSender())
    container.register("EMAIL", lambda: EmailSender())
    container.register("PUSH", lambda: PushSender())

    while True:
        main_menu()
        option = input("Choose an option: ")

        if option == "1":
            name = input("Enter name: ")
            recipient = input("Enter recipient (phone/email/device): ")
            provider_key = choose_channel()

            try:
                notifier = container.resolve(provider_key)
                user_service = UserRegistrationService(notifier)
                user_service.register_user(name, recipient)
            except ValueError as e:
                print(f"[Error] {e}")
        elif option == "2":
            print("Exiting.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    """
    Run the application if executed as a script.
    """
    main()
