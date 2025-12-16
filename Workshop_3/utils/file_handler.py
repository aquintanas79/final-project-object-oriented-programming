import json
from Workshop_3.models.connection import Connection

class FileHandler:
    """
    CRC Card: File Handler
    Responsibility: Read/Write files, validate integrity.
    """

    # ======================================
    # SAVE CIRCUIT DESIGN
    # ======================================
    def save_design(self, board, filename):
        data = {
            "components": [],
            "connections": []
        }

        # Save components
        for c in board.components:
            data["components"].append({
                "id": c.id,
                "name": c.name,
                "type": c.get_type(),
                "x": c.x,
                "y": c.y
            })

        # Save connections
        for conn in board.connections:
            data["connections"].append({
                "a": conn.component_a.name,
                "b": conn.component_b.name
            })

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        print(f"[OK] Circuit saved to {filename}")
        return True

    # ======================================
    # LOAD CIRCUIT DESIGN
    # ======================================
    def load_design(self, board, component_library, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except Exception as e:
            print(f"[ERROR] Loading file: {e}")
            return False

        # Clear current board
        board.components.clear()
        board.connections.clear()

        # Recreate components
        for comp in data["components"]:
            new_comp = component_library.create_component(
                comp["type"],
                comp["id"],
                comp["name"]
            )
            new_comp.x = comp["x"]
            new_comp.y = comp["y"]
            board.add_component(new_comp)

        # Recreate connections
        for conn in data["connections"]:
            a = next(c for c in board.components if c.name == conn["a"])
            b = next(c for c in board.components if c.name == conn["b"])
            board.add_connection(Connection(a, b))

        print(f"[OK] Circuit loaded from {filename}")
        return True
