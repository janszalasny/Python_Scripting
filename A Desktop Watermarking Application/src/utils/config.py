# src/utils/config.py

from pathlib import Path  # <-- 1. IMPORT THIS
from patterns.singleton import SingletonMeta

class ConfigManager(metaclass=SingletonMeta):
    """
    Singleton configuration manager for the application.
    Stores and provides access to application-wide settings.
    """
    def __init__(self):
        # --- START OF CHANGE ---
        # Build an absolute path to the assets directory from this file's location.
        # This makes the path independent of the current working directory.
        project_root = Path(__file__).parent.parent.parent
        self.default_font_path = str(project_root / "assets" / "fonts" / "Roboto-Bold.ttf")
        # --- END OF CHANGE ---

        self.default_font_size = 48
        self.default_text_color = "#ffffff"
        self.default_opacity = 0.5
        self.default_position = "center"

    def get(self, key, default=None):
        """Gets a configuration value by key."""
        return getattr(self, key, default)