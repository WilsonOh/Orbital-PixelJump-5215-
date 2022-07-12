import pygame

from pixeljump.level import Level
from pixeljump.background import Background
from pixeljump.enemies import MushroomEnemy, FroggyEnemy
from pixeljump.tile import Tile2, EnemyTile, TreeTile, PropTile, Rain
from pixeljump.player import Player
from pixeljump.settings import load_settings
from pixeljump.assets import select_background_act, get_map, get_assets_path
from pixeljump.spikes import Spike
from pixeljump.camera import Camera
from pixeljump.target import Target

settings = load_settings()

TILE_SIZE = settings["window"]["tile_size"]
WINDOW_WIDTH = settings["window"]["screen_width"]
WINDOW_HEIGHT = settings["window"]["screen_height"]

get_background = select_background_act(2)


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
        self.main_background = get_background("background_sky")
        self.backgrounds = [
            Background(
                scaling=0.25,
                pos=(0, 200),
                image=get_background("far_clouds", scale=(2, 1))
            ),
            Background(
                scaling=0.50,
                pos=(0, 400),
                image=get_background("close_clouds", scale=(2, 1))
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
                    self.target = Target((x, y), self.visible_sprites)

                if col == "#":
                    PropTile((x, y), self.visible_sprites)

                if col == "R":
                    Rain((x, y), self.active_sprites, col=1,
                         visible_sprites=self.visible_sprites,
                         active_sprites=self.active_sprites)

                if col.isnumeric():
                    Tile2(
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
            act=2,
            collision_sprites=self.collision_sprites,
            visible_sprites=self.visible_sprites,
            active_sprites=self.active_sprites,
        )

    def play_bgm(self, path: str) -> None:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

