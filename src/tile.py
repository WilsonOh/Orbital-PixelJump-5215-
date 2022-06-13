import os

import pygame

from settings import load_settings

settings = load_settings()
TILE_SIZE = settings["window"]["tile_size"]
TILE_COLOR = settings["colors"]["tile"]

ASSETS_PATH = os.path.abspath("../assets/")


class Tile(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int], *groups: pygame.sprite.AbstractGroup):
        super().__init__(*groups)
        self.image = pygame.transform.scale(
            pygame.image.load(ASSETS_PATH + "/dirt.png"), (64, 64)
        )
        self.rect = self.image.get_rect(topleft=position)
