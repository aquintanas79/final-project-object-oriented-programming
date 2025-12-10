class Component:
    def __init__(self, name):
        self.name = name
        self.state = False

    def toggle(self):
        pass


class Switch(Component):
    def toggle(self):
        self.state = not self.state


class Light(Component):
    def update_state(self, signal):
        self.state = signal

