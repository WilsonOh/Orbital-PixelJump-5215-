import pygame
from settings import load_settings


settings = load_settings()
TILE_SIZE = settings['window']['tile_size']
TILE_COLOR = settings['colors']['tile']


class Tile(pygame.sprite.Sprite):

    def __init__(self, position: tuple[int, int], *groups: pygame.sprite.AbstractGroup):
        super().__init__(*groups)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=position)
        self.image.fill(TILE_COLOR)

