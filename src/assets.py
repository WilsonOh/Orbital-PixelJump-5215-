from typing import Optional
import pygame
from pathlib import Path

ASSETS_PATH = Path(__file__).parents[1].resolve() / "assets/"


def get_background(
    background_name: str,
    scale: tuple[int, int],
    *,
    colorkey: Optional[tuple[int, int, int]] = None,
    convert=True,
) -> pygame.surface.Surface:
    backgrounds_path = ASSETS_PATH / "layers/"
    background_image_path = backgrounds_path / (background_name + ".png")
    if convert:
        background = pygame.transform.scale(
            pygame.image.load(background_image_path), scale
        ).convert()
    else:
        background = pygame.transform.scale(
            pygame.image.load(background_image_path), scale
        )
    background.set_colorkey(colorkey)
    return background


def get_sprite_image(
    asset_name: str, scale: tuple[int, int], convert=True
) -> pygame.surface.Surface:
    asset_path = ASSETS_PATH / (asset_name + ".png")
    if convert:
        asset = pygame.transform.scale(pygame.image.load(asset_path), scale).convert()
    else:
        asset = pygame.transform.scale(pygame.image.load(asset_path), scale)
    asset.set_colorkey((255, 255, 255))
    return asset


def get_map() -> list[list[str]]:
    with open(ASSETS_PATH / "map.txt") as f:
        return [list(row) for row in f.readlines()]
