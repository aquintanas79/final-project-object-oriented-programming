class HelpSystem:
    """
    CRC Card: Help System
    Responsibility: Tooltips, tutorials.
    """
    def show_tooltip(self, component_type):
        tooltips = {
            "Resistor": "Limits current flow.",
            "Light": "Emits light when powered."
        }
        return tooltips.get(component_type, "No help available.")