class HelpSystem:
    def __init__(self):
        self._tips = {
            "Resistor": "Used to limit current in circuits.",
            "Relay": "Acts as a switch controlled by electricity."
        }

    def show_help(self, component_name):
        return self._tips.get(component_name, "No help available for this component.")
