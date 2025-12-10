class Component:
    def __init__(self, name):
        self.name = name

    def get_state(self):
        raise NotImplementedError


class Switch(Component):
    def __init__(self, name):
        super().__init__(name)
        self.state = False

    def toggle(self):
        self.state = not self.state

    def get_state(self):
        return self.state


class Light(Component):
    def __init__(self, name):
        super().__init__(name)
        self.state = False

    def update(self, signal):
        self.state = signal

    def get_state(self):
        return self.state
