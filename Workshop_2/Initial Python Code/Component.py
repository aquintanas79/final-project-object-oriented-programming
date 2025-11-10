from abc import ABC, abstractmethod

class Component(ABC):
    def __init__(self, comp_id, comp_type):
        self._id = comp_id
        self._type = comp_type
        self._connections = []

    @abstractmethod
    def simulate(self):
        pass

class Resistor(Component):
    def __init__(self, comp_id, resistance):
        super().__init__(comp_id, "Resistor")
        self._resistance = resistance

    def simulate(self):
        return f"Simulating resistor with {self._resistance}Ω resistance."

class Sensor(Component):
    def __init__(self, comp_id, sensor_type):
        super().__init__(comp_id, "Sensor")
        self._sensor_type = sensor_type

    def simulate(self):
        return f"Simulating sensor of type {self._sensor_type}."

class Relay(Component):
    def __init__(self, comp_id, state=False):
        super().__init__(comp_id, "Relay")
        self._state = state

    def simulate(self):
        return f"Relay is {'ON' if self._state else 'OFF'}."
