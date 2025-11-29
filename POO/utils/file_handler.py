class FileHandler:
    """
    CRC Card: File Handler
    Responsibility: Read/Write files, validate integrity.
    """
    def save_project(self, filename, data):
        print(f"Saving project to {filename}.json...")
        # Lógica real de guardado JSON iría aquí
        return True

    def load_project(self, filename):
        print(f"Loading project from {filename}...")
        return {} # Retorna datos dummy