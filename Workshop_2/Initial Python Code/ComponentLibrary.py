class ComponentLibrary:
    def __init__(self):
        self._available_components = ["Resistor", "Sensor", "Relay", "Microcontroller"]

    def get_available_components(self):
        return self._available_components
