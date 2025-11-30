from Workshop_3.models.circuit_board import CircuitBoard
from Workshop_3.logic.simulation_engine import SimulationEngine
from Workshop_3.views.ui_manager import UIManager
from Workshop_3.views.monitor import Monitor
from Workshop_3.models.component_library import ComponentLibrary
import json

class UIController:
    """
    CRC Card: UI Controller
    Responsibility: Interpret actions, coordinate UI-Logic-Data.
    """
    def __init__(self):
        # Inicializa las partes del sistema
        self.board = CircuitBoard()
        self.engine = SimulationEngine()
        self.ui_manager = UIManager()
        self.monitor = Monitor()
        self.library = ComponentLibrary()

    def handle_add_component(self, type_name, name):
        # 1. Busca en la librería
        new_comp = self.library.create_component(type_name, f"ID_{name}", name)
        # 2. Agrega al modelo (Board)
        if new_comp:
            self.board.add_component(new_comp)
            # 3. Actualiza la vista
            self.ui_manager.render_board(self.board)

    def handle_run_simulation(self):
        # 1. Obtiene datos del modelo
        comps, conns = self.board.get_data_for_simulation()
        # 2. Manda a calcular al motor
        self.engine.calculate(comps, conns)
        # 3. Manda resultados al monitor
        self.monitor.update_table(comps)

    def handle_create_connection(self, comp_a, comp_b):
        conn = self.board.create_connection(comp_a, comp_b)
        return conn is not None

    def save_design(self, filename="circuit_design.json"):
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

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        print("Circuit saved successfully.")
        return True


    def load_design(self, filename="circuit_design.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except:
            print("Error loading file.")
            return False

        # Reset board
        self.board.components.clear()
        self.board.connections.clear()

        # Create components
        for comp in data["components"]:
            type_name = comp["type"]
            new_comp = self.library.create_component(
                type_name,
                comp["id"],
                comp["name"]
            )
            new_comp.x = comp["x"]
            new_comp.y = comp["y"]
            self.board.add_component(new_comp)

        # Recreate connections
        for c in data["connections"]:
            a = next(x for x in self.board.components if x.name == c["a"])
            b = next(x for x in self.board.components if x.name == c["b"])
            from Workshop_3.models.connection import Connection
            self.board.add_connection(Connection(a, b))

        print("Design loaded successfully.")
        return True
