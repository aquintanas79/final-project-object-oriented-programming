class Connection:
    """
    CRC Card: Connection
    Responsibility: Link components, verify validity.
    """
    def __init__(self, component_a, component_b):
        self.component_a = component_a
        self.component_b = component_b

    def verify_validity(self):
        return (
            self.component_a is not None and
            self.component_b is not None and
            self.component_a != self.component_b
        )
