
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
)

class CircuitGUI(QWidget):

    def __init__(self, circuit, file_manager):
        super().__init__()
        self.circuit = circuit
        self.file_manager = file_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Domotic Simulator")

        layout = QVBoxLayout()

        self.label = QLabel("No simulation yet")
        layout.addWidget(self.label)

        btn_sim = QPushButton("Run Simulation")
        btn_sim.clicked.connect(self.run_simulation)
        layout.addWidget(btn_sim)

        btn_save = QPushButton("Save Circuit")
        btn_save.clicked.connect(self.save)
        layout.addWidget(btn_save)

        btn_load = QPushButton("Load Circuit")
        btn_load.clicked.connect(self.load)
        layout.addWidget(btn_load)

        self.setLayout(layout)

    def run_simulation(self):
        self.circuit.simulate()
        states = ", ".join(
            f"{c.name}: {c.get_state()}" for c in self.circuit.components
        )
        self.label.setText(states)

    def save(self):
        self.file_manager.save(self.circuit)
        self.label.setText("Circuit saved")

    def load(self):
        self.file_manager.load(self.circuit)
        self.label.setText("Circuit loaded")
