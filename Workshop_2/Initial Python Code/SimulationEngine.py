class SimulationEngine:
    def __init__(self, circuit_board):
        self._circuit_board = circuit_board

    def run_simulation(self):
        print("Starting simulation...")
        self._circuit_board.simulate()
        print("Simulation finished.")
