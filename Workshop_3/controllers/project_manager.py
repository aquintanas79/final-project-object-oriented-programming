from utils.file_handler import FileHandler

class ProjectManager:
    """
    CRC Card: Project Manager
    Responsibility: CRUD projects, auto-save.
    """
    def __init__(self):
        self.file_handler = FileHandler()
        self.current_project = None

    def save_current_project(self):
        if self.current_project:
            self.file_handler.save_project(self.current_project, {})
        else:
            print("No project open to save.")
