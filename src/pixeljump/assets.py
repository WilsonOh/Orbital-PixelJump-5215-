import pygame
from pathlib import Path

ASSETS_PATH = Path(__file__).parent.resolve() / "assets/"


def get_background(
    background_name: str,
    scale: tuple[int, int],
    *,
    colorkey: tuple[int, int, int] | None = None,
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


def get_music(asset_name: str) -> pygame.mixer.Sound:
    asset_path = ASSETS_PATH / "music" / asset_name
    return pygame.mixer.Sound(asset_path)


def get_assets_path() -> str:
    return str(ASSETS_PATH) + "/"


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


def get_animation_image(
    asset_name: str, animation_name: str, scale: tuple[int, int], convert=True
) -> pygame.surface.Surface:
    asset_path = ASSETS_PATH / animation_name / (asset_name + ".png")
    if convert:
        asset = pygame.transform.scale(pygame.image.load(asset_path), scale).convert()
    else:
        asset = pygame.transform.scale(pygame.image.load(asset_path), scale)
    asset.set_colorkey((255, 255, 255))
    return asset


def get_map(map: str) -> list[list[str]]:
    with open(ASSETS_PATH / "maps" / f"{map}.txt") as f:
        return [list(row) for row in f.readlines()]
