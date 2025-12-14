classDiagram
    %% --- CAPA DE VISTA (VIEW LAYER) ---
    class DomoticDragDropGUI {
        -UIController controller
        -QGraphicsScene scene
        -Dict item_to_model
        +add_component_to_scene(type, x, y)
        +run_simulation()
        +update_visuals()
    }

    class GraphicsComponentItem {
        -Component model_ref
        -QColor color
        +paint()
        +mouseMoveEvent()
    }
    
    class Monitor {
        +display_results(voltage, current)
        +log_event(message)
    }

    %% --- CAPA DE CONTROLADOR (CONTROLLER LAYER) ---
    class UIController {
        -CircuitBoard board
        -SimulationEngine engine
        -ProjectManager project_manager
        -ComponentLibrary library
        -Monitor monitor
        +handle_add_component(type)
        +handle_connection(id_a, id_b)
        +run_circuit_simulation()
    }

    class ProjectManager {
        -FileHandler file_handler
        -dict current_project
        +save_current_project()
        +load_project(path)
    }

    %% --- CAPA DE INFRAESTRUCTURA (INFRASTRUCTURE) ---
    class User {
        -String username
        -String password
        +login(password) bool
    }

    class SettingManager {
        -dict settings
        +load_settings()
    }

    class FileHandler {
        +save_project(data, path)
        +read_json(path)
    }

    %% --- CAPA DE MODELO (MODEL LAYER) ---
    class CircuitBoard {
        -List~Component~ components
        -List~Connection~ connections
        +add_component(Component)
        +create_connection(id_a, id_b)
        +get_component_by_id(id)
    }

    class SimulationEngine {
        +calculate(components, connections)
        +check_short_circuits()
    }

    class Connection {
        +Component node_a
        +Component node_b
        +bool is_active
    }
    
    class ComponentLibrary {
        +get_available_types()
        +create_instance(type)
    }

    %% --- JERARQUÍA DE COMPONENTES (HEART OF THE PROJECT) ---
    class Component {
        <<Abstract>>
        #String id
        #String name
        #String type
        #float x, y
        #float voltage
        +get_type()* String
        +to_dict()
    }

    class Resistor {
        +float resistance
        +get_type()
    }
    class Light {
        +bool is_on
        +get_type()
    }
    class Switch {
        +bool is_open
        +toggle()
        +get_type()
    }
    class Capacitor {
        +float capacitance
        +get_type()
    }
    class Diode {
        +float forward_voltage
        +get_type()
    }
    class Sensor {
        +float threshold
        +detect()
        +get_type()
    }
    class Relay {
        +bool state
        +switch_circuit()
        +get_type()
    }

    %% --- RELACIONES PRECISAS ---
    
    %% View interactions
    DomoticDragDropGUI --> UIController : "1. User Action"
    DomoticDragDropGUI *-- GraphicsComponentItem : "Contains"
    GraphicsComponentItem --> Component : "Maps to"

    %% Controller management
    UIController --> CircuitBoard : "Modifies"
    UIController --> SimulationEngine : "Triggers"
    UIController --> ProjectManager : "Delegates I/O"
    UIController --> Monitor : "Updates"
    UIController ..> ComponentLibrary : "Uses"

    %% Project & Data interactions
    ProjectManager --> FileHandler : "Uses"
    
    %% Main execution flow
    User ..> DomoticDragDropGUI : "Accesses"
    SettingManager ..> DomoticDragDropGUI : "Configures"

    %% Core Model structure
    CircuitBoard o-- Component : "Aggregates"
    CircuitBoard *-- Connection : "Composes"
    Connection --> Component : "Links"

    %% Inheritance (Polymorphism)
    Component <|-- Resistor
    Component <|-- Light
    Component <|-- Switch
    Component <|-- Capacitor
    Component <|-- Diode
    Component <|-- Sensor
    Component <|-- Relay
