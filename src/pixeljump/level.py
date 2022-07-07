import pygame
from abc import ABC, abstractmethod

from pixeljump.player import Player
from pixeljump.assets import get_background, get_assets_path
from pixeljump.camera import Camera
from pixeljump.background import Background


class Level(ABC):
    def __init__(self):
        self.player: Player
        self.window = pygame.display.get_surface()
        self.map: list[list[str]]
        # Updated every frame
        self.active_sprites = pygame.sprite.Group()
        # Drawn every frame
        self.visible_sprites = Camera()
        # Checks for collision every frame
        self.enemy_sprites = pygame.sprite.Group()
        self.enemy_collision_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.particle_sprites = pygame.sprite.Group()
        self.play_bgm(get_assets_path() + "music/music.wav")
        self.setup_level()
        self.main_background = get_background(
            "parallax-mountain-bg",
        )
        self.backgrounds: list[Background]

    @abstractmethod
    def setup_level(self):
        pass

    def play_bgm(self, path: str) -> None:
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    @abstractmethod
    def update_sprite(self):
        pass

    @abstractmethod
    def run(self, clock: pygame.time.Clock):
        pass
