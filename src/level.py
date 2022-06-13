import os

import pygame

from player import Player
from settings import load_level_map, load_settings
from tile import Tile

settings = load_settings()
level_map = load_level_map()

LEVEL_MAP = level_map["1"]
TILE_SIZE = settings["window"]["tile_size"]
WINDOW_WIDTH = settings["window"]["screen_width"]
WINDOW_HEIGHT = settings["window"]["screen_height"]

BACKGROUND_PATH = os.path.abspath("../assets/layers/")


class Level:
    def __init__(self):
        self.player: Player
        self.window = pygame.display.get_surface()
        # Updated every frame
        self.active_sprites = pygame.sprite.Group()
        # Drawn every frame
        self.visible_sprites = Camera()
        # Checks for collision every frame
        self.collision_sprites = pygame.sprite.Group()
        self.setup_level()
        self.FAR_MOUNTAIN = pygame.transform.scale(
            pygame.image.load(BACKGROUND_PATH + "/far.png"),
            (WINDOW_WIDTH, WINDOW_HEIGHT),
        ).convert()
        self.FAR_MOUNTAIN.set_colorkey((255, 255, 255))

        self.CLOSE_MOUNTAIN = pygame.transform.scale(
            pygame.image.load(BACKGROUND_PATH + "/close.png"),
            (WINDOW_WIDTH * 2, WINDOW_HEIGHT),
        )

        self.FOREGROUND = pygame.transform.scale(
            pygame.image.load(BACKGROUND_PATH + "/foreground.png"),
            (WINDOW_WIDTH * 2, WINDOW_HEIGHT),
        ).convert()
        self.FOREGROUND.set_colorkey((255, 255, 255))

        self.TREES = pygame.transform.scale(
            pygame.image.load(BACKGROUND_PATH + "/trees.png"),
            (WINDOW_WIDTH * 2, WINDOW_HEIGHT),
        )
        self.backgrounds = [
            [
                0.25,
                [100, 50, self.FAR_MOUNTAIN],
            ],
            [
                0.25,
                [300, 20, self.CLOSE_MOUNTAIN],
            ],
            [
                0.50,
                [50, 20, self.TREES],
            ],
            [
                0.75,
                [250, 50, self.FOREGROUND],
            ],
        ]

    def setup_level(self):
        for row_idx, row in enumerate(LEVEL_MAP):
            for col_idx, col in enumerate(row):
                x = col_idx * TILE_SIZE
                y = row_idx * TILE_SIZE
                if col == "#":
                    Tile((x, y), self.visible_sprites, self.collision_sprites)
                if col == "P":
                    self.player = Player(
                        (x, y),
                        self.visible_sprites,
                        self.active_sprites,
                        collision_sprites=self.collision_sprites,
                    )

    def run(self):
        self.window.blit(
            pygame.transform.scale(
                pygame.image.load(BACKGROUND_PATH + "/parallax-mountain-bg.png"),
                (WINDOW_WIDTH, WINDOW_HEIGHT),
            ),
            (0, 0),
        )
        self.visible_sprites.draw(self.window, self.player, self.backgrounds)
        self.visible_sprites.update(self.player)
        self.active_sprites.update()


class Camera(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.offset: pygame.Vector2 = pygame.Vector2(0, 0)

    def draw(self, surface: pygame.Surface, player: Player, backgrounds) -> None:
        for background in backgrounds:
            surface.blit(
                background[1][2],
                (
                    background[1][0] - self.offset.x * background[0],
                    background[1][1] - self.offset.y * background[0],
                ),
            )
        for sprite in self:
            surface.blit(sprite.image, sprite.rect.topleft - self.offset)

    def update(self, player: Player) -> None:
        self.offset.x += (
            (player.rect.x - self.offset.x) - ((WINDOW_WIDTH // 2) + (TILE_SIZE // 2))
        ) // 20

        self.offset.y += (
            (player.rect.y - self.offset.y) - ((WINDOW_HEIGHT // 2) + (TILE_SIZE // 2))
        ) // 20
