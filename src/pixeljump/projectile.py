import pygame
from typing import Literal
from pixeljump.settings import load_settings

from pixeljump.spikes import Spike

settings = load_settings()

TILE_SIZE = settings["window"]["tile_size"]


class Projectile(pygame.sprite.Sprite):

    horizontal_velocity = 10

    def __init__(
        self,
        pos: tuple[int, int],
        *groups: pygame.sprite.AbstractGroup,
        direction: Literal["right", "left"],
        collision_sprites: pygame.sprite.Group,
        enemy_sprites: pygame.sprite.Group
    ) -> None:
        super().__init__(*groups)
        self.image = pygame.Surface((TILE_SIZE // 5, TILE_SIZE // 5))
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill(pygame.Color("black"))
        self.direction: int = 1 if direction == "right" else -1
        self.collision_sprites = collision_sprites
        self.enemy_sprites = enemy_sprites

    def move(self) -> None:
        self.rect.x += self.horizontal_velocity * self.direction

    def check_collision(self) -> None:
        for sprite in self.collision_sprites:
            assert sprite.rect is not None
            if self.rect.colliderect(sprite.rect):
                self.kill()
        for enemy in self.enemy_sprites:
            assert enemy.rect is not None
            if self.rect.colliderect(enemy.rect):
                if type(enemy) != Spike:
                    enemy.kill()
                self.kill()

    def update(self) -> None:
        self.move()
        self.check_collision()
