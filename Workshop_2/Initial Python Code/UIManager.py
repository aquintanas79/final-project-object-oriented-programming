class UIManager:
    def __init__(self):
        self._theme = "Light"

    def display_message(self, message):
        print(f"[UI Message] {message}")

    def change_theme(self, theme):
        self._theme = theme
