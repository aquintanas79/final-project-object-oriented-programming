class User:
    """
    CRC Card: User
    Responsibility: Auth, manage projects access.
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_logged_in = False

    def login(self, input_pass):
        if input_pass == self.password:
            self.is_logged_in = True
            print(f"User {self.username} logged in.")
            return True
        return False