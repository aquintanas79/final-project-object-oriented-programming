class Connection:
    def __init__(self, start_component, end_component):
        self._start = start_component
        self._end = end_component

    def validate(self):
        return self._start != self._end
