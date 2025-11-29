from models.circuit_board import CircuitBoard
from logic.simulation_engine import SimulationEngine
from views.ui_manager import UIManager
from views.monitor import Monitor
from models.component_library import ComponentLibrary

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
