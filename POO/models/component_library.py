from models.concrete_components import Resistor, Light

class ComponentLibrary:
    """
    CRC Card: Component Library
    Responsibility: Store available types, default properties.
    """
    def get_available_components(self):
        return ["Resistor", "Light", "Switch", "Sensor"]

    def create_component(self, type_name, id, name):
        if type_name == "Resistor":
            return Resistor(id, name, 0, 0, resistance=100)
        elif type_name == "Light":
            return Light(id, name, 0, 0)
        return None