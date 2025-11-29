class CircuitBoard:
    """
    CRC Card: Circuit Board
    Responsibility: Manage layout, handle connections, send data to engine.
    """
    def __init__(self):
        self.components = [] # Agregación de Componentes
        self.connections = [] # Agregación de Conexiones

    def add_component(self, component):
        self.components.append(component)
    
    def add_connection(self, connection):
        if connection.verify_validity():
            self.connections.append(connection)

    def get_data_for_simulation(self):
        return self.components, self.connections
