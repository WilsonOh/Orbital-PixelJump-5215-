import json

SETTINGS_PATH = "./settings.json"
LEVEL_MAP_PATH = "./level_map.json"


def load_settings() -> dict:
    with open(SETTINGS_PATH) as f:
        settings = json.load(f)
        return settings


def load_level_map() -> dict:
    with open(LEVEL_MAP_PATH) as f:
        level_map = json.load(f)
        return level_map
