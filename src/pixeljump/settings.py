import json
from pathlib import Path

root_dir = Path(__file__).parent.resolve()
SETTINGS_PATH = root_dir / "settings"


def load_settings() -> dict:
    with open(SETTINGS_PATH / "settings.json") as f:
        settings = json.load(f)
        return settings
