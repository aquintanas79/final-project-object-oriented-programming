class SettingManager:
    """
    CRC Card: Setting Manager
    Responsibility: Preferences (theme, language).
    """
    def __init__(self):
        self.theme = "Dark"
        self.auto_save_interval = 5 # minutos

    def load_settings(self):
        print("Settings loaded.")