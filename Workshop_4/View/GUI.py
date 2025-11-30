import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QLabel,
    QListWidget, QVBoxLayout, QHBoxLayout, QMessageBox,
    QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsSimpleTextItem,
    QGraphicsLineItem, QSplitter
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QPen

# Import controller
from Workshop_3.controllers.ui_controller import UIController


# ============================
#   VISUAL GRAPHICS ITEM
# ============================
class GraphicsComponentItem(QGraphicsRectItem):
    WIDTH = 80
    HEIGHT = 40

    def __init__(self, comp_type, comp_name, controller, model_comp=None):
        super().__init__(0, 0, self.WIDTH, self.HEIGHT)

        self.comp_type = comp_type
        self.comp_name = comp_name
        self.controller = controller
        self.model_comp = model_comp

        self.setBrush(QBrush(Qt.GlobalColor.lightGray))
        self.setPen(QPen(Qt.GlobalColor.black))

        self.setFlags(
            QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable |
            QGraphicsRectItem.GraphicsItemFlag.ItemIsSelectable
        )

        # LABEL
        self.label = QGraphicsSimpleTextItem(comp_name, parent=self)
        self.label.setPos(8, 10)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        if self.model_comp:
            pos = self.scenePos()
            self.model_comp.x = pos.x()
            self.model_comp.y = pos.y()


# ============================
#   MAIN GUI
# ============================
class DomoticDragDropGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Domotic Circuit Simulator — Drag & Drop")
        self.setGeometry(150, 150, 1350, 720)

        self.controller = UIController()

        # Connection mode
        self.connect_mode = False
        self.first_selected_model = None

        # MAIN LAYOUT
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout()
        central.setLayout(main_layout)

        # =====================================
        #  LEFT PANEL
        # =====================================
        left_panel = QWidget()
        left_layout = QVBoxLayout()
        left_panel.setLayout(left_layout)

        left_layout.addWidget(QLabel("Component Library"))

        # Component buttons
        self.btn_add_resistor = QPushButton("Add Resistor")
        self.btn_add_light = QPushButton("Add Light")
        self.btn_add_switch = QPushButton("Add Switch")
        self.btn_add_capacitor = QPushButton("Add Capacitor")
        self.btn_add_diode = QPushButton("Add Diode")

        self.btn_connect = QPushButton("Connect Components")
        self.btn_delete = QPushButton("Delete Component")

        # NEW BUTTONS: SAVE / LOAD
        self.btn_save = QPushButton("Save Circuit")
        self.btn_load = QPushButton("Load Circuit")

        # Connect buttons
        self.btn_add_resistor.clicked.connect(lambda: self.add_component("Resistor"))
        self.btn_add_light.clicked.connect(lambda: self.add_component("Light"))
        self.btn_add_switch.clicked.connect(lambda: self.add_component("Switch"))
        self.btn_add_capacitor.clicked.connect(lambda: self.add_component("Capacitor"))
        self.btn_add_diode.clicked.connect(lambda: self.add_component("Diode"))

        self.btn_connect.clicked.connect(self.enable_connect_mode)
        self.btn_delete.clicked.connect(self.delete_component)

        self.btn_save.clicked.connect(self.save_design)
        self.btn_load.clicked.connect(self.load_design)

        # Add widgets
        left_layout.addWidget(self.btn_add_resistor)
        left_layout.addWidget(self.btn_add_light)
        left_layout.addWidget(self.btn_add_switch)
        left_layout.addWidget(self.btn_add_capacitor)
        left_layout.addWidget(self.btn_add_diode)

        left_layout.addSpacing(15)
        left_layout.addWidget(self.btn_connect)
        left_layout.addWidget(self.btn_delete)

        left_layout.addSpacing(15)
        left_layout.addWidget(self.btn_save)
        left_layout.addWidget(self.btn_load)

        left_layout.addStretch()

        # =====================================
        #  CENTER VIEW
        # =====================================
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHints(self.view.renderHints())

        # =====================================
        #  RIGHT PANEL
        # =====================================
        right_panel = QWidget()
        right_layout = QVBoxLayout()
        right_panel.setLayout(right_layout)

        right_layout.addWidget(QLabel("Board Components"))
        self.list_components = QListWidget()
        right_layout.addWidget(self.list_components)

        right_layout.addWidget(QLabel("Simulation Output"))
        self.sim_output = QListWidget()
        right_layout.addWidget(self.sim_output)

        self.btn_simulate = QPushButton("Run Simulation")
        self.btn_simulate.clicked.connect(self.run_simulation)
        right_layout.addWidget(self.btn_simulate)

        # =====================================
        #  SPLITTER
        # =====================================
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(left_panel)
        splitter.addWidget(self.view)
        splitter.addWidget(right_panel)
        splitter.setStretchFactor(1, 2)

        main_layout.addWidget(splitter)

        # Mapping visual → model
        self.item_to_model = {}

    # =============================================
    #  DRAW CONNECTION LINES
    # =============================================
    def _draw_connections(self):
        # Remove previous connection lines
        for item in list(self.scene.items()):
            if isinstance(item, QGraphicsLineItem):
                self.scene.removeItem(item)

        pen = QPen(Qt.GlobalColor.darkBlue, 3)

        for conn in getattr(self.controller.board, "connections", []):
            try:
                a = conn.component_a
                b = conn.component_b
                x1, y1 = a.x + 40, a.y + 20
                x2, y2 = b.x + 40, b.y + 20
                self.scene.addLine(x1, y1, x2, y2, pen)
            except:
                continue

    # =============================================
    #  ADD COMPONENT
    # =============================================
    def add_component(self, type_name):
        name = f"{type_name}_{len(self.controller.board.components) + 1}"

        try:
            self.controller.handle_add_component(type_name, name)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to add component: {e}")
            return

        model = self.controller.board.components[-1]

        item = GraphicsComponentItem(type_name, model.name, self.controller, model)
        item.setPos(200, 200)
        self.scene.addItem(item)

        self.list_components.addItem(f"{model.name} ({type_name})")
        self.item_to_model[item] = model

        self._draw_connections()

    # =============================================
    #  CONNECTION MODE
    # =============================================
    def enable_connect_mode(self):
        QMessageBox.information(self, "Connect Mode",
                                "Select TWO components from the list to connect.")
        self.connect_mode = True
        self.first_selected_model = None

        try:
            self.list_components.itemClicked.disconnect(self.process_connect_click)
        except:
            pass

        self.list_components.itemClicked.connect(self.process_connect_click)

    def process_connect_click(self, item_clicked):
        if not self.connect_mode:
            return

        comp_name = item_clicked.text().split(" ")[0]
        model = next((c for c in self.controller.board.components if c.name == comp_name), None)

        if model is None:
            QMessageBox.warning(self, "Error", "Invalid selection.")
            self._end_connect_mode()
            return

        if not self.first_selected_model:
            self.first_selected_model = model
            QMessageBox.information(self, "Connect Mode",
                                    f"First component selected: {model.name}")
            return

        second = model

        if second == self.first_selected_model:
            QMessageBox.warning(self, "Error", "Cannot connect a component to itself.")
            self._end_connect_mode()
            return

        # Try connection
        ok = False
        try:
            ok = bool(self.controller.handle_create_connection(
                self.first_selected_model, second
            ))
        except:
            ok = False

        self._end_connect_mode()

        if not ok:
            QMessageBox.warning(self, "Connection Error", "Connection failed.")
            return

        QMessageBox.information(self, "Connected", "Components successfully connected!")
        self._draw_connections()

    def _end_connect_mode(self):
        self.connect_mode = False
        self.first_selected_model = None
        try:
            self.list_components.itemClicked.disconnect(self.process_connect_click)
        except:
            pass

    # =============================================
    #  DELETE COMPONENT
    # =============================================
    def delete_component(self):
        selected = self.list_components.currentItem()
        if not selected:
            QMessageBox.warning(self, "Delete", "Select a component first.")
            return

        name = selected.text().split(" ")[0]

        model = next((c for c in self.controller.board.components if c.name == name), None)
        if not model:
            return

        self.controller.board.components.remove(model)

        self.controller.board.connections = [
            c for c in self.controller.board.connections
            if c.component_a != model and c.component_b != model
        ]

        to_remove = [item for item, m in self.item_to_model.items() if m == model]
        for item in to_remove:
            self.scene.removeItem(item)
            del self.item_to_model[item]

        self.list_components.takeItem(self.list_components.currentRow())
        self._draw_connections()

    # =============================================
    #  SIMULATION
    # =============================================
    def run_simulation(self):
        for item, model in self.item_to_model.items():
            pos = item.scenePos()
            model.x = pos.x()
            model.y = pos.y()

        self.controller.handle_run_simulation()

        self.sim_output.clear()
        for comp in self.controller.board.components:
            self.sim_output.addItem(
                f"{comp.name}: {comp.voltage:.2f} V   {comp.current:.4f} A"
            )

        self._draw_connections()

    # =============================================
    #  SAVE CIRCUIT
    # =============================================
    def save_design(self):
        ok = self.controller.save_design("circuit_design.json")
        if ok:
            QMessageBox.information(self, "Saved", "Circuit saved successfully.")

    # =============================================
    #  LOAD CIRCUIT
    # =============================================
    def load_design(self):
        ok = self.controller.load_design("circuit_design.json")
        if not ok:
            QMessageBox.warning(self, "Error", "Failed to load design.")
            return

        # clear scene
        self.scene.clear()
        self.list_components.clear()
        self.item_to_model.clear()

        # Recreate graphics
        for model in self.controller.board.components:
            item = GraphicsComponentItem(model.get_type(), model.name, self.controller, model)
            item.setPos(model.x, model.y)
            self.scene.addItem(item)
            self.item_to_model[item] = model
            self.list_components.addItem(f"{model.name} ({model.get_type()})")

        self._draw_connections()
        QMessageBox.information(self, "Loaded", "Circuit loaded successfully!")
