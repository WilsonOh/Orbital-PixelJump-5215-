from pixeljump.assets import get_assets_path, get_background, get_map
from pixeljump.enemies import FroggyEnemy, MushroomEnemy
from pixeljump.player import Player
from pixeljump.settings import load_settings
from pixeljump.spikes import Spike
from pixeljump.tile import EnemyTile, PropTile, Tile, TreeTile
import pygame

settings = load_settings()

LEVEL_MAP = get_map()
TILE_SIZE = settings["window"]["tile_size"]
WINDOW_WIDTH = settings["window"]["screen_width"]
WINDOW_HEIGHT = settings["window"]["screen_height"]


class Level:
    def __init__(self):
        self.player: Player
        self.window = pygame.display.get_surface()
        # Updated every frame
        self.active_sprites = pygame.sprite.Group()
        # Drawn every frame
        self.visible_sprites = Camera()
        # Checks for collision every frame
        self.enemy_sprites = pygame.sprite.Group()
        self.enemy_collision_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.play_bgm(get_assets_path() + "music/music.wav")
        self.setup_level()
        self.main_background = get_background(
            "parallax-mountain-bg",
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            colorkey=((255, 255, 255)),
        )
        self.backgrounds = [
            [
                0.15,
                [
                    100,
                    100,
                    get_background(
                        "far", (WINDOW_WIDTH, WINDOW_HEIGHT), colorkey=(255, 255, 255)
                    ),
                ],
            ],
            [
                0.25,
                [
                    300,
                    100,
                    get_background(
                        "close",
                        (WINDOW_WIDTH * 2, WINDOW_HEIGHT),
                        colorkey=(255, 255, 255),
                    ),
                ],
            ],
            [
                0.50,
                [
                    50,
                    100,
                    get_background(
                        "trees",
                        (WINDOW_WIDTH * 2, WINDOW_HEIGHT),
                        colorkey=(255, 255, 255),
                    ),
                ],
            ],
            [
                0.75,
                [
                    250,
                    250,
                    get_background(
                        "foreground",
                        (WINDOW_WIDTH * 2, WINDOW_HEIGHT),
                        colorkey=(255, 255, 255),
                    ),
                ],
            ],
        ]

    def setup_level(self):
        p_x = 0
        p_y = 0
        for row_idx, row in enumerate(LEVEL_MAP):
            for col_idx, col in enumerate(row):
                x = col_idx * TILE_SIZE
                y = row_idx * TILE_SIZE
                """
                if col == "D":
                    Tile((x, y), self.visible_sprites, self.collision_sprites)
                if col == "G":
                    Tile(
                        (x, y), self.visible_sprites, self.collision_sprites, grass=True
                    )
                """
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
                if col == "#":
                    PropTile((x, y), self.visible_sprites)

                if col == "$":
                    self.target = Target((x, y))

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
            collision_sprites=self.collision_sprites,
        )

    def play_bgm(self, path: str) -> None:
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    def run(self, clock: pygame.time.Clock):
        self.window.blit(self.main_background, (0, 0))
        self.visible_sprites.draw(self.window, self.backgrounds, clock)
        self.visible_sprites.update(self.player)
        self.active_sprites.update()
        self.enemy_sprites.update()


class Camera(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.offset: pygame.Vector2 = pygame.Vector2(0, 0)

    def draw(
        self, surface: pygame.surface.Surface, backgrounds, clock: pygame.time.Clock
    ) -> None:
        for background in backgrounds:
            surface.blit(
                background[1][2],
                (
                    background[1][0] - self.offset.x * background[0],
                    background[1][1] - self.offset.y * background[0],
                ),
            )
        for sprite in self:
            if sprite.rect is not None and sprite.image is not None:
                sprite_topleft = pygame.Vector2(sprite.rect.topleft)
                surface.blit(sprite.image, sprite_topleft - self.offset)
        font_size = int(pygame.display.get_surface().get_width() * 0.03)
        font = pygame.font.SysFont("Arial", font_size, True)
        text = font.render(f"FPS: {clock.get_fps():.2f}", True, pygame.Color("red"))
        surface.blit(text, (0, 0))

    def update(self, player: Player) -> None:
        if player.rect is not None:
            self.offset.x += (
                (player.rect.x - self.offset.x) - (WINDOW_WIDTH // 2 + TILE_SIZE // 2)
            ) // 20

            self.offset.y += (
                (player.rect.y - self.offset.y) - (WINDOW_HEIGHT // 2 + TILE_SIZE // 2)
            ) // 20


class Target(pygame.sprite.Sprite):
    def __init__(
        self, pos: tuple[int, int], *groups: pygame.sprite.AbstractGroup
    ) -> None:
        super().__init__(*groups)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=pos)