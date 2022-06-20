from pathlib import Path
import pygame
from settings import load_settings

settings = load_settings()
TILE_SIZE = settings["window"]["tile_size"]
TILE_COLOR = settings["colors"]["tile"]

ASSETS_PATH = Path(__file__).parents[1].resolve() / "assets/"


class Tile(pygame.sprite.Sprite):
    def __init__(
        self,
        position: tuple[int, int],
        *groups: pygame.sprite.AbstractGroup,
        grass=False
    ):
        super().__init__(*groups)
        if grass:
            self.image = pygame.transform.scale(
                pygame.image.load(ASSETS_PATH / "grass.png"), (64, 64)
            )
        else:
            self.image = pygame.transform.scale(
                pygame.image.load(ASSETS_PATH / "dirt.png"), (64, 64)
            )
        self.rect = self.image.get_rect(topleft=position)


class EnemyTile(Tile):
    def __init__(
        self,
        position: tuple[int, int],
        *groups: pygame.sprite.AbstractGroup,
        grass=False
    ):
        super().__init__(position, *groups, grass=grass)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=position)
        self.image.fill(pygame.Color("red"))
