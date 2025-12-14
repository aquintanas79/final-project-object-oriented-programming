# Domotic Circuit Simulator

## 1. Project Description
This project is the Final Course Project for **Object-Oriented Programming (OOP)**. It is a desktop application developed in **Python** that allows users to design, simulate, and manage simple domotic (home automation) circuits.

The system implements a **Layered Architecture** (MVC Pattern) and strictly follows **SOLID principles** and **OOP concepts** (Inheritance, Polymorphism, Encapsulation, Abstraction).

### Key Features
* **Drag & Drop Interface:** Easily place components on the circuit board.
* **Component Library:** Includes Resistors, Lights, Switches, Capacitors, Diodes, Sensors, and Relays.
* **Circuit Simulation:** Real-time calculation of basic electrical states (On/Off, Voltage check).
* **Persistence:** Save and load circuit designs using JSON format.
* **User Management:** Basic authentication system (Login).

---

## 2. Prerequisites & Dependencies
To run this project, you need the following installed on your system:

* **Python 3.8+**
* **PyQt6** (External library for the Graphical User Interface)

### External Libraries Used
* `PyQt6`: Used for `QtWidgets`, `QtGui`, and `QtCore` to handle the GUI and events.
* `json`: Native Python library for data persistence.
* `abc`: Native Python library for Abstract Base Classes.

---

## 3. Installation & How to Run

Follow these steps to set up the environment and run the simulator:

1.  **Clone or Download the Repository** to your local machine.
2.  **Open the terminal** (Command Prompt or PowerShell) in the project root folder.
3.  **Install the required library** using pip:
    ```bash
    pip install PyQt6
    ```
4.  **Run the application**:
    ```bash
    python main.py
    ```
    *(Note: Ensure you are running the command from the root directory where `main.py` is located).*

---

## 4. User Manual

### Step 1: Login
* When the application starts, enter the default credentials:
    * **Username:** `admin`
    * **Password:** `1234`

### Step 2: Designing a Circuit
1.  **Add Components:** On the main window, click the buttons on the toolbar (e.g., "Add Resistor", "Add Light", "Add Sensor") or select them from the menu to place them on the board.
2.  **Move Components:** Click and drag any component to position it.
3.  **Connect Components:** * Hold `Ctrl` and click on **Component A**.
    * Then, click on **Component B**.
    * A line will appear connecting them.

### Step 3: Simulation & Control
* **Run Simulation:** Click the "Run" or "Play" button to calculate voltages and check the status of the circuit.
* **Interacting:** * **Switches:** Click on a Switch component to toggle it Open/Closed.
    * **Sensors:** Click on a Sensor to simulate a "Trigger" event (Motion detected).
    * **Relays:** Relays will automatically switch state if the input voltage exceeds the threshold.
* **Feedback:** The console (Monitor) will display the simulation results (e.g., "Light is ON").

### Step 4: Save & Load
* **Save:** Go to `File > Save Project` to store your current design as a JSON file.
* **Load:** Go to `File > Open Project` to restore a previously saved circuit.

---

## 5. System Architecture
The project is structured into three main layers:
* **Views (GUI):** Handles user input and rendering (`DomoticDragDropGUI`).
* **Controllers:** Manages logic flow and updates models (`UIController`).
* **Models:** Defines the data and business logic (`CircuitBoard`, `SimulationEngine`, `Component` hierarchy).

---

## Authors
* **Arley Leonardo Quintana Sepulveda** - Electrical Engineering Student
* **Juan Esteban Rincón Zambrano** - Electrical Engineering Student
* **Maria Paula Betancourth Hernández** - Electrical Engineering Student

* Course: Object-Oriented Programming (2025-II)
* University: Universidad Nacional de Colombia
