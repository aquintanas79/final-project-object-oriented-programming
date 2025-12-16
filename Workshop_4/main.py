# main.py
import sys
from PyQt6.QtWidgets import *

from Workshop_4.View.GUI import DomoticDragDropGUI
from Workshop_3.utils.setting_manager import SettingManager
from Workshop_3.models.user import User


def main():
    print("--- DOMOTIC CIRCUIT SIMULATOR v1.0 ---")

    # 1. Load application settings
    settings = SettingManager()
    settings.load_settings()

    # 2. User login
    current_user = User("admin", "1234")
    if not current_user.login("1234"):
        print("Login failed.")
        return

    # 3. Start GUI application
    app = QApplication(sys.argv)
    window = DomoticDragDropGUI()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
