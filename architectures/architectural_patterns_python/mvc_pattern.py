
# --- Model ---
class UserModel:
    def __init__(self, name: str):
        self.name = name
    def get_user_data(self) -> str:
        return f"User: {self.name}"

# --- View ---
class UserView:
    def display_user(self, user_info: str) -> None:
        print(f"[View] {user_info}")

# --- Controller ---
class UserController:
    def __init__(self, model: UserModel, view: UserView):
        self._model = model
        self._view = view

    def update_view(self) -> None:
        # Get data from model
        user_data = self._model.get_user_data()
        # Pass data to view
        self._view.display_user(user_data)

# Example usage
model = UserModel("Alice")
view = UserView()
controller = UserController(model, view)

# Controller acts as a bridge between Model and View
controller.update_view()