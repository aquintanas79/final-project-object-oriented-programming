class CircuitBoard:
    def __init__(self):
        self._components = []
        self._connections = []

    def add_component(self, component):
        self._components.append(component)

    def connect(self, c1, c2):
        connection = Connection(c1, c2)
        if connection.validate():
            self._connections.append(connection)
        else:
            print("Invalid connection detected.")

    def simulate(self):
        for comp in self._components:
            print(comp.simulate())
