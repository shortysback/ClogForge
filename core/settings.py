import json
import os

SETTINGS_FILE = "data/settings.json"


def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {}

    try:
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}


def save_settings(settings):
    os.makedirs("data", exist_ok=True)

    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)