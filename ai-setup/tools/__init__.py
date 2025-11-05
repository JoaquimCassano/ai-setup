from ..constants import SETTINGS_PATH
import json

def load_settings():
    try:
      with open(SETTINGS_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Settings file not found. Please run the setup process.")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from settings file. Maybe you changed it manually?")