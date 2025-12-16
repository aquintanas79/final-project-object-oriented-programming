from Workshop_3.models.circuit_board import CircuitBoard
from Workshop_3.logic.simulation_engine import SimulationEngine
from Workshop_3.views.ui_manager import UIManager
from Workshop_3.views.monitor import Monitor
from Workshop_3.models.component_library import ComponentLibrary
from Workshop_3.models.connection import Connection
import json


class UIController:
    """
    CRC Card: UI Controller
    Responsibility: Interpret actions, coordinate UI-Logic-Data.
    """

    def __init__(self):
        self.board = CircuitBoard()
        self.engine = SimulationEngine()
        self.ui_manager = UIManager()
        self.monitor = Monitor()
        self.library = ComponentLibrary()

    # =============================================
    #  COMPONENT MANAGEMENT
    # =============================================
    def handle_add_component(self, type_name, name):
        new_comp = self.library.create_component(type_name, f"ID_{name}", name)
        if new_comp:
            self.board.add_component(new_comp)
            self.ui_manager.render_board(self.board)

    def handle_create_connection(self, comp_a, comp_b):
        conn = self.board.create_connection(comp_a, comp_b)
        return conn is not None

    # =============================================
    #  SIMULATION
    # =============================================
    def handle_run_simulation(self):
        comps, conns = self.board.get_data_for_simulation()
        self.engine.calculate(comps, conns)
        self.monitor.update_table(comps)

    # =============================================
    #  SAVE / LOAD DESIGN  (ITEM 4)
    # =============================================
    def save_design(self, filepath):
        data = {
            "components": [
                {
                    "id": c.id,
                    "name": c.name,
                    "type": c.get_type(),
                    "x": c.x,
                    "y": c.y
                }
                for c in self.board.components
            ],
            "connections": [
                {
                    "a": conn.component_a.name,
                    "b": conn.component_b.name
                }
                for conn in self.board.connections
            ]
        }

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        return True

    def load_design(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            return False

        # Reset board
        self.board.components.clear()
        self.board.connections.clear()

        # Recreate components
        for comp in data.get("components", []):
            new_comp = self.library.create_component(
                comp["type"],
                comp["id"],
                comp["name"]
            )
            new_comp.x = comp.get("x", 0)
            new_comp.y = comp.get("y", 0)
            self.board.add_component(new_comp)

        # Recreate connections
        for conn in data.get("connections", []):
            a = next(c for c in self.board.components if c.name == conn["a"])
            b = next(c for c in self.board.components if c.name == conn["b"])
            self.board.add_connection(Connection(a, b))

        return True
