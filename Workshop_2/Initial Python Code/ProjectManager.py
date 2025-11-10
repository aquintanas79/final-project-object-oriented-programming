class ProjectManager:
    def __init__(self, file_handler):
        self._file_handler = file_handler
        self._current_project = None

    def create_project(self, name):
        self._current_project = {"name": name, "components": []}

    def save_project(self, path):
        if self._current_project:
            self._file_handler.write(path, self._current_project)

    def open_project(self, path):
        self._current_project = self._file_handler.read(path)
