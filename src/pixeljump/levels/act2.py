import pygame

from pixeljump.level import Level
from pixeljump.background import Background
from pixeljump.enemies import MushroomEnemy, FroggyEnemy
from pixeljump.tile import Tile, EnemyTile, TreeTile, PropTile
from pixeljump.player import Player
from pixeljump.settings import load_settings
from pixeljump.assets import get_background, get_map, get_assets_path
from pixeljump.spikes import Spike
from pixeljump.camera import Camera
from pixeljump.target import Target

settings = load_settings()

TILE_SIZE = settings["window"]["tile_size"]
WINDOW_WIDTH = settings["window"]["screen_width"]
WINDOW_HEIGHT = settings["window"]["screen_height"]


class ActTwo(Level):
    def __init__(self):
        self.player: Player
        self.window = pygame.display.get_surface()
        self.map = get_map("map_empty")
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
        self.play_bgm(get_assets_path() + "music/BossBattle.wav")
        self.setup_level()
        self.main_background = get_background("act2/background_sky", scale=(1, 1))
        self.backgrounds = [
            Background(
                scaling=0.15, pos=(300, 100), image=get_background("act2/far_clouds")
            ),
            Background(
                scaling=0.50, pos=(100, 100), image=get_background("act2/close_clouds")
            ),
        ]

    def setup_level(self):
        p_x = 0
        p_y = 0
        for row_idx, row in enumerate(self.map):
            for col_idx, col in enumerate(row):
                x = col_idx * TILE_SIZE
                y = row_idx * TILE_SIZE
                if col == "P":
                    p_x = x
                    p_y = y
                if col == "E":
                    MushroomEnemy(
                        (x, y),
                        self.enemy_sprites,
                        self.visible_sprites,
                        collision_sprites=self.collision_sprites,
                        enemy_collision_sprites=self.enemy_collision_sprites,
                        player_sprite=self.player_sprite,
                    )
                if col == "F":
                    FroggyEnemy(
                        (x, y),
                        self.enemy_sprites,
                        self.visible_sprites,
                        collision_sprites=self.collision_sprites,
                        enemy_collision_sprites=self.enemy_collision_sprites,
                        player_sprite=self.player_sprite,
                    )

                if col == "I":
                    EnemyTile((x, y), self.enemy_collision_sprites)
                if col == "T":
                    TreeTile((x, y), self.visible_sprites)

                if col == "S":
                    Spike(
                        (x, y + 30),
                        self.enemy_sprites,
                        self.visible_sprites,
                        collision_sprites=self.collision_sprites,
                        enemy_collision_sprites=self.enemy_collision_sprites,
                        player_sprite=self.player_sprite,
                    )

                if col == "$":
                    self.target = Target((x, y))

                if col == "#":
                    PropTile((x, y), self.visible_sprites)

                if col.isnumeric():
                    Tile(
                        (x, y),
                        self.visible_sprites,
                        self.collision_sprites,
                        col=int(col),
                    )
        self.player = Player(
            (p_x, p_y),
            self.visible_sprites,
            self.active_sprites,
            self.player_sprite,
            target=self.target,
            particle_sprites=self.particle_sprites,
            collision_sprites=self.collision_sprites,
        )

    def play_bgm(self, path: str) -> None:
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    def update_sprite(self):
        for particles in self.particle_sprites:
            self.visible_sprites.add(particles)
            self.particle_sprites.remove(particles)

    def run(self, clock: pygame.time.Clock):
        self.window.blit(self.main_background, (0, 0))
        self.visible_sprites.draw(self.window, self.backgrounds, clock)
        self.visible_sprites.update(self.player)
        self.active_sprites.update()
        self.enemy_sprites.update()
        self.update_sprite()
