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
        col=1,
    ):
        super().__init__(*groups)
        """
        if grass:
            self.image = pygame.transform.scale(
                pygame.image.load(ASSETS_PATH / "grass.png"), (64, 64)
            ).convert()
        else:
            self.image = pygame.transform.scale(
                pygame.image.load(ASSETS_PATH / "dirt.png"), (64, 64)
            ).convert()
        """
        self.image = pygame.image.load(
            get_assets_path() + "TILES/" + str(col) + ".png"
        ).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(topleft=position)


class EnemyTile(Tile):
    def __init__(
        self, position: tuple[int, int], *groups: pygame.sprite.AbstractGroup, col=1
    ):
        super().__init__(position, *groups, col=col)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=position)
        self.image.fill(pygame.Color("red"))


class TreeTile(Tile):
    def __init__(
        self, position: tuple[int, int], *groups: pygame.sprite.AbstractGroup, col=1
    ):
        super().__init__(position, *groups, col=col)
        self.tree1 = get_sprite_image("tree1", [256, 273])
        self.tree2 = get_sprite_image("tree2", [256, 273])
        self.tree3 = get_sprite_image("tree3", [256, 273])
        self.house1 = get_sprite_image("house1", [256, 273])
        self.image = random.choice([self.tree1, self.tree2, self.tree3, self.house1])
        self.rect = self.image.get_rect(center=position)


class PropTile(Tile):
    def __init__(
        self, position: tuple[int, int], *groups: pygame.sprite.AbstractGroup, col=1
    ):
        super().__init__(position, *groups, col=col)
        self.bush1 = get_sprite_image("bush1", [64, 69])
        self.bush2 = get_sprite_image("bush2", [64, 69])
        self.crate1 = get_sprite_image("crate1", [64, 69])
        self.skull1 = get_sprite_image("skull1", [64, 69])
        self.skull2 = get_sprite_image("skull2", [64, 64])
        self.shroom1 = get_sprite_image("shroom1", [64, 69])
        self.sign1 = get_sprite_image("sign1", [64, 69])
        self.image = random.choice(
            [
                self.bush1,
                self.bush2,
                self.crate1,
                self.skull1,
                self.skull2,
                self.shroom1,
                self.shroom1,
            ]
        )
        self.rect = self.image.get_rect(topleft=position)
