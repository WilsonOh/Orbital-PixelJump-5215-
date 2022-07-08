import pygame

pygame.init()

from pixeljump.assets import ASSETS_PATH
from pixeljump.settings import SETTINGS_PATH
from pathlib import Path

ROOT = Path(__file__).parents[1].resolve()


def test_assets_path():
    assert ASSETS_PATH == Path(str(ROOT) + "/src/pixeljump/assets")


def test_settings_path():
    assert SETTINGS_PATH == Path(str(ROOT) + "/src/pixeljump/settings")
