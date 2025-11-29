class Connection:
    """
    CRC Card: Connection
    Responsibility: Link components, verify validity.
    """
    def __init__(self, component_a, component_b):
        self.component_a = component_a
        self.component_b = component_b
        self.is_valid = True

    def verify_validity(self):
        # Lógica simple de validación
        if self.component_a == self.component_b:
            self.is_valid = False
            print("Error: Short circuit detected (Same component connected to itself)")
        return self.is_valid