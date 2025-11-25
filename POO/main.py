# main.py
from models.user import User
from controllers.ui_controller import UIController
from utils.setting_manager import SettingManager

def main():
    print("--- DOMOTIC CIRCUIT SIMULATOR v1.0 ---\n")

    # 1. Cargar configuraciones
    settings = SettingManager()
    settings.load_settings()

    # 2. Login de Usuario
    current_user = User("admin", "1234")
    if not current_user.login("1234"):
        return

    # 3. Iniciar el Controlador Principal
    app = UIController()

    # 4. Simulación de Interacción del Usuario
    print("\n--- User Action: Drag & Drop Components ---")
    app.handle_add_component("Resistor", "R1_Main")
    app.handle_add_component("Light", "L1_Kitchen")

    print("\n--- User Action: Press Simulate ---")
    app.handle_run_simulation()

if __name__ == "__main__":
    main()      