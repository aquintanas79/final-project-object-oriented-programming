class Circuit:
    def __init__(self):
        self.components = []
        self.connections = []

    def add_component(self, component):
        self.components.append(component)

    def connect(self, source, target):
        self.connections.append((source, target))

    def simulate(self):
        for source, target in self.connections:
            if hasattr(target, "update"):
                target.update(source.get_state())
