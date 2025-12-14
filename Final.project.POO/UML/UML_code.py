classDiagram
    %% Capa de Vista (View)
    class DomoticDragDropGUI {
        +UIController controller
        +QGraphicsScene scene
        +add_component(type)
        +run_simulation()
        +save_design()
        +load_design()
    }

    class GraphicsComponentItem {
        +Component model_comp
        +paint()
    }

    %% Capa de Controlador (Controller)
    class UIController {
        +CircuitBoard board
        +SimulationEngine engine
        +ComponentLibrary library
        +handle_add_component()
        +handle_run_simulation()
        +save_design()
        +load_design()
    }

    %% Capa de Lógica de Negocio (Logic)
    class SimulationEngine {
        +calculate(components, connections)
    }

    %% Capa de Modelo (Model)
    class CircuitBoard {
        +List~Component~ components
        +List~Connection~ connections
        +add_component(Component)
        +create_connection(comp_a, comp_b)
        +get_data_for_simulation()
    }

    class Connection {
        +Component component_a
        +Component component_b
        +verify_validity() bool
    }

    class Component {
        <<Abstract>>
        #str id
        #str name
        #float x
        #float y
        #float voltage
        #float current
        +move(x, y)
        +rotate()
        +get_type()* str
    }

    %% Componentes Concretos (Herencia)
    class Resistor {
        +float resistance
        +get_type()
    }
    class Light {
        +bool is_on
        +get_type()
    }
    class Switch {
        +bool state
        +get_type()
    }
    class Capacitor {
        +float capacitance
        +get_type()
    }

    %% Relaciones
    DomoticDragDropGUI --> UIController : "Usa"
    DomoticDragDropGUI *-- GraphicsComponentItem : "Contiene visualmente"
    GraphicsComponentItem o-- Component : "Referencia modelo"
    
    UIController --> CircuitBoard : "Gestiona"
    UIController --> SimulationEngine : "Usa"
    UIController ..> ComponentLibrary : "Crea componentes con"

    CircuitBoard o-- Component : "Agregación"
    CircuitBoard *-- Connection : "Composición"
    
    Connection --> Component : "Conecta"

    Component <|-- Resistor : "Herencia"
    Component <|-- Light : "Herencia"
    Component <|-- Switch : "Herencia"
    Component <|-- Capacitor : "Herencia"
