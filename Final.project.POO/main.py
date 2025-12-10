
from View.GUI import CircuitGUI
from Model.circuit import Circuit
from Data.file_manager import FileManager
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication([])
    circuit = Circuit()
    file_manager = FileManager()

    gui = CircuitGUI(circuit, file_manager)
    gui.show()
    app.exec_()

if __name__ == "__main__":
    main()
