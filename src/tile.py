from pathlib import Path
import pygame
from settings import load_settings
from assets import get_assets_path, get_sprite_image
import random

settings = load_settings()
TILE_SIZE = settings["window"]["tile_size"]
TILE_COLOR = settings["colors"]["tile"]

ASSETS_PATH = Path(__file__).parents[1].resolve() / "assets/"


class Tile(pygame.sprite.Sprite):
    def __init__(
        self,
        position: tuple[int, int],
        *groups: pygame.sprite.AbstractGroup,
        col = 1,
    ):
        super().__init__(*groups)
        '''
        if grass:
            self.image = pygame.transform.scale(
                pygame.image.load(ASSETS_PATH / "grass.png"), (64, 64)
            ).convert()
        else:
            self.image = pygame.transform.scale(
                pygame.image.load(ASSETS_PATH / "dirt.png"), (64, 64)
            ).convert()
        '''
        self.image = pygame.image.load(get_assets_path() + "TILES/" + str(col) + ".png").convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect(topleft=position)


class EnemyTile(Tile):
    def __init__(
        self,
        position: tuple[int, int],
        *groups: pygame.sprite.AbstractGroup,
        col=1
    ):
        super().__init__(position, *groups, col=col)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=position)
        self.image.fill(pygame.Color("red"))


class TreeTile(Tile):
    def __init__(
        self,
        position: tuple[int, int],
        *groups: pygame.sprite.AbstractGroup,
        col=1
    ):
        super().__init__(position, *groups, col=col)
        self.tree1 = get_sprite_image("tree1", [128, 128])
        self.tree2 = get_sprite_image("tree2", [128, 128])
        self.tree3 = get_sprite_image("tree3", [128, 128])
        self.image = random.choice([self.tree1, self.tree2, self.tree3])
        self.rect = self.image.get_rect(topleft=position)


