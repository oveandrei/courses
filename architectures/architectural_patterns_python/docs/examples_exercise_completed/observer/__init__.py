from logic import Stock, StockLogger, StockView, ThresholdAlert, Helper

def client():
    """
    Entry point for running the Observer Pattern demo.
    - Creates a stock (subject)
    - Initializes several observers (logger, view, threshold alerts)
    - Allows attaching/detaching observers dynamically
    - Simulates stock price changes
    """
    
    # Create a stock instance with initial price
    apple = Stock('AAPL', 145.2)

    # Create observer instances
    logger = StockLogger('logger')
    stock_view = StockView('stock view')
    threshold_low = ThresholdAlert(135, 'below')
    threshold_above = ThresholdAlert(175, "above")

    # Initialize helper for user interaction logic
    helper = Helper()

    # Attach observers initially
    apple.attach(logger)
    apple.attach(stock_view)
    apple.attach(threshold_low)
    apple.attach(threshold_above)

    # Dictionary mapping observer names to instances
    observers: dict = {
        'logger': logger,
        'stock view': stock_view,
        'threshold_low': threshold_low,
        'threshold_above': threshold_above
    }

    # Display initial stock price
    print("------Initial Price-------")
    print(f"AAPL starting price: {apple._price:.2f}")

    # Main interactive loop
    while True:
        print("------------------------------------------------")
        print("1. Attach Observers.")
        print("2. Detach Observers.")
        print("3. Set a new stock price.")
        print("4. Exit")

        response = input("Choose a number: ")
        print("------------------------------------------------")

        if response == '1':
            # Attach observers not already attached
            helper.list_available(apple, observers)
            choice = input("Enter observer name to attach: ").strip().lower()
            obs = observers.get(choice)
            if obs and obs not in apple._observers:
                apple.attach(obs)
                print(f"Attached {choice}")
            else:
                print("Invalid or already attached.")

        elif response == '2':
            # Detach currently attached observers
            helper.list_attached(apple)
            choice = input("Enter observer name to detach: ").strip().lower()
            obs = observers.get(choice)
            if obs and obs in apple._observers:
                apple.detach(obs)
                print(f"Detached {choice}")
            else:
                print("Invalid or not currently attached.")

        elif response == '3':
            # Simulate new stock price update
            response = helper.validate_stock_price(input("Please enter the new price of AAPL: ")) # Validates the response using the helper class
            if response == 'wrong type':
                print("Your response MUST be number of type FLOAT or INTEGER.")
            else:
                apple.set_price(response) # type: ignore

        elif response == '4':
            # Exit program
            break

        else:
            print("Please choose a number from the list.")
            continue

        print("--------------------------------------------------")


if __name__ == '__main__':
    client()
