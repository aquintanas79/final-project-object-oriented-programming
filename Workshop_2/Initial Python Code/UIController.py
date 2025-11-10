class UIController:
    def __init__(self):
        self._selected_component = None

    def select_component(self, component):
        self._selected_component = component

    def rotate_component(self):
        if self._selected_component:
            print(f"Component {self._selected_component._id} rotated.")

    def delete_component(self):
        if self._selected_component:
            print(f"Component {self._selected_component._id} deleted.")
