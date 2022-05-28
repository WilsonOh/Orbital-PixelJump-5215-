import pygame
from settings import load_settings, load_level_map
from tile import Tile
from player import Player

settings = load_settings()
level_map = load_level_map()

LEVEL_MAP = level_map["1"]
TILE_SIZE = settings['window']['tile_size']


class Level:

    def __init__(self):
        self.window = pygame.display.get_surface()
        # Updated every frame
        self.active_sprites = pygame.sprite.Group()
        # Drawn every frame
        self.visible_sprites = pygame.sprite.Group()
        # Checks for collision every frame
        self.collision_sprites = pygame.sprite.Group()
        self.setup_level()

    def setup_level(self):
        for row_idx, row in enumerate(LEVEL_MAP):
            for col_idx, col in enumerate(row):
                x = col_idx * TILE_SIZE
                y = row_idx * TILE_SIZE
                if col == '#':
                    Tile((x, y), self.visible_sprites, self.collision_sprites)
                if col == 'P':
                    Player((x, y), self.visible_sprites, self.active_sprites,
                           collision_sprites=self.collision_sprites)

    def run(self):
        self.visible_sprites.draw(self.window)
        self.active_sprites.update()
