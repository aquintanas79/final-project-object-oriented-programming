from models.component import Component

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