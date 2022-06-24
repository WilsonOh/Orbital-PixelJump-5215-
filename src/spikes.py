import pygame
from enemies import Enemy
from assets import get_sprite_image

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
        self.image = get_sprite_image("spikes", [60, 40])

    def checkPlayer(self):
        for player in self.player_sprite:
            if self.rect.colliderect(player.rect):
                player.player_die()

    def update(self):
        self.checkPlayer()
