from Workshop_3.models.concrete_components import (
    Resistor, Light, Capacitor, Diode, Switch
)

class ComponentLibrary:
    """
    CRC Card: Component Library
    Responsibility: Store available types, default properties.
    """

    def get_available_components(self):
        return ["Resistor", "Light", "Switch", "Capacitor", "Diode"]

    def create_component(self, type_name, id, name):

        if type_name == "Resistor":
            return Resistor(id, name, 0, 0, resistance=100)

        elif type_name == "Light":
            return Light(id, name, 0, 0)

        elif type_name == "Switch":
            # Switch requiere: (id, x, y)
            return Switch(id, 0, 0)

        elif type_name == "Capacitor":
            # Capacitor requiere: (id, x, y)
            return Capacitor(id, 0, 0)

        elif type_name == "Diode":
            # Diode requiere: (id, x, y)
            return Diode(id, 0, 0)

        return None
