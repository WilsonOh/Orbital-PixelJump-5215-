import pygame
from pixeljump.enemies import Enemy
from pixeljump.assets import get_sprite_image
from pixeljump.player import Player


class Spike(Enemy):
    def __init__(
        self,
        pos: tuple[int, int],
        *groups: pygame.sprite.AbstractGroup,
        collision_sprites: pygame.sprite.Group,
        enemy_collision_sprites: pygame.sprite.Group,
        player_sprite: pygame.sprite.Group
    ) -> None:
        super().__init__(
            pos,
            *groups,
            collision_sprites=collision_sprites,
            enemy_collision_sprites=enemy_collision_sprites,
            player_sprite=player_sprite,
        )
        self.image = get_sprite_image("spikes1", (60, 42))

    def update(self):
        self.checkPlayer()
