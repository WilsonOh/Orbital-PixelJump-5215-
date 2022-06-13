import json
from pathlib import Path

root_dir = Path(__file__).parents[1].resolve()
SETTINGS_PATH = root_dir / "settings/settings.json"
LEVEL_MAP_PATH = root_dir / "settings/level_map.json"


def load_settings() -> dict:
    with open(SETTINGS_PATH) as f:
        settings = json.load(f)
        return settings


def load_level_map() -> dict:
    with open(LEVEL_MAP_PATH) as f:
        level_map = json.load(f)
        return level_map
