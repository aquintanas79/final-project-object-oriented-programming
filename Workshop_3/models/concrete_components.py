from Workshop_3.models.component import Component

class Resistor(Component):
    def __init__(self, id, name, x, y, resistance):
        super().__init__(id, name, x, y)
        self.resistance = resistance

    def get_type(self):
        return "Resistor"

class Light(Component):
    def __init__(self, id, name, x, y):
        super().__init__(id, name, x, y)
        self.is_on = False

    def get_type(self):
        return "Light"


class Capacitor(Component):
    def __init__(self, id, x, y, capacitance=10e-6):
        super().__init__(id, f"C{id}", x, y)
        self.capacitance = capacitance

    def get_type(self):
        return "Capacitor"


class Diode(Component):
    def __init__(self, id, x, y):
        super().__init__(id, f"D{id}", x, y)

    def get_type(self):
        return "Diode"


class Switch(Component):
    def __init__(self, id, x, y):
        super().__init__(id, f"SW{id}", x, y)
        self.state = False

    def get_type(self):
        return "Switch"