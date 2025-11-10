class User:
    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._projects = []

    def authenticate(self, input_user, input_pass):
        """Validate user credentials."""
        return self._username == input_user and self._password == input_pass

    def add_project(self, project):
        self._projects.append(project)
