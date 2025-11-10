class SettingManager:
    def __init__(self):
        self._language = "English"
        self._autosave_time = 5  # minutes

    def update_setting(self, name, value):
        setattr(self, f"_{name}", value)
