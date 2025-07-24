from abc import ABC, abstractmethod
import weakref


class Observer(ABC):
    """
    Abstract base class for all observers.
    Observers must implement the `update` method.
    """
    @abstractmethod
    def update(self, context: dict):
        """
        Called when the subject (Stock) notifies observers of a change.
        :param context: Dictionary containing updated stock data.
        """
        pass


class Stock:
    """
    The Subject in the Observer pattern.
    Represents a stock and notifies observers when its price changes.
    """
    def __init__(self, symbol: str, price: float) -> None:
        self._symbol = symbol
        self._price = price
        # WeakSet allows observers to be garbage collected if no longer referenced
        self._observers = weakref.WeakSet()

    def attach(self, observer: Observer):
        """Attach an observer to the stock."""
        self._observers.add(observer)

    def detach(self, observer: Observer):
        """Detach an observer from the stock."""
        self._observers.discard(observer)

    def notify(self):
        """Notify all attached observers of a price change."""
        data = {
            "symbol": self._symbol,
            "price": self._price
        }
        for observer in self._observers:
            observer.update(data)

    def set_price(self, new_price: float):
        """
        Set a new stock price and notify observers if the price changed.
        :param new_price: New stock price to set.
        """
        if self._price != new_price:
            self._price = new_price
            self.notify()

    @property
    def symbol(self):
        """Read-only access to the stock symbol."""
        return self._symbol

    @property
    def price(self):
        """Read-only access to the stock price."""
        return self._price


class ThresholdAlert(Observer):
    """
    Observer that alerts if the stock price crosses a given threshold
    either above or below, depending on configuration.
    """
    def __init__(self, threshold: float, direction: str, name=None) -> None:
        """
        :param threshold: Price threshold to monitor.
        :param direction: 'above' or 'below'.
        :param name: Optional display name for UI/debugging.
        """
        self.threshold = threshold
        self.direction = direction
        self._prev_state = None  # Used to detect transitions
        self.name = name or f"ThresholdAlert ({direction} {threshold})"

    def update(self, context: dict) -> None:
        current = (
            context['price'] > self.threshold
            if self.direction == "above"
            else context['price'] < self.threshold
        )

        # Initial state: alert if already across the threshold
        if self._prev_state is None:
            if current:
                self._print_alert(context)
            self._prev_state = current
            return

        # Alert only on crossing the threshold
        if current and not self._prev_state:
            self._print_alert(context)

        self._prev_state = current

    def _print_alert(self, context):
        direction_str = "above" if self.direction == "above" else "below"
        print(f"[ALERT] {context['symbol']} crossed ${self.threshold:.2f} "
              f"({direction_str})! Current: ${context['price']:.2f}")


class StockView(Observer):
    """
    Observer that displays the current stock price to a UI.
    """
    def __init__(self, name: str):
        self.name = name

    def update(self, context: dict) -> None:
        print(f"[VIEW] {context['symbol']} - ${context['price']:.2f}")


class StockLogger(Observer):
    """
    Observer that logs the stock price updates (e.g., to console or file).
    """
    def __init__(self, name: str):
        self.name = name

    def update(self, context: dict) -> None:
        print(f"[LOG] {context['symbol']} - ${context['price']:.2f}")


class Helper:
    """
    Utility class for handling user input validation and observer management.
    """

    def validate_stock_price(self, response: str) -> float | str:
        """
        Validates whether a user input is a valid stock price.
        :param response: User input string.
        :return: Float if valid, or 'wrong type' if not.
        """
        try:
            return float(response)
        except ValueError:
            return 'wrong type'

    def list_attached(self, stock: Stock):
        """
        Print a list of currently attached observers for a stock.
        :param stock: The stock whose observers should be listed.
        """
        print("\nCurrently attached observers:")
        for obs in stock._observers:
            print(f" - {getattr(obs, 'name', type(obs).__name__)}")

    def list_available(self, stock: Stock, all_observers: dict):
        """
        Print a list of observers not yet attached to the stock.
        :param stock: The stock to compare against.
        :param all_observers: All observer instances with user-friendly names.
        """
        attached_set = set(stock._observers)
        print("\nAvailable observers to attach:")
        for name, obs in all_observers.items():
            if obs not in attached_set:
                print(f" - {name}")
