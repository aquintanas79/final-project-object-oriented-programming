class Monitor:
    def __init__(self):
        self._data = {}

    def update_values(self, node, value):
        self._data[node] = value

    def show_data(self):
        for node, value in self._data.items():
            print(f"Node {node}: {value}V")
