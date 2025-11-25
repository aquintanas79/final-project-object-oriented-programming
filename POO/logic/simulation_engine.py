class SimulationEngine:
    """
    CRC Card: Simulation Engine
    Responsibility: Calculate electrical values, detect errors.
    """
    def calculate(self, components, connections):
        print("--- Engine: Calculating Voltages and Currents ---")
        # Simulación Dummy de Ley de Ohm
        for comp in components:
            if comp.get_type() == "Resistor":
                comp.voltage = 5.0 # Valor simulado
                comp.current = comp.voltage / comp.resistance
            elif comp.get_type() == "Light":
                comp.voltage = 5.0
        return True