import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(
        self,
        pos: tuple[int, int],
        *groups: pygame.sprite.AbstractGroup,
        collision_sprites: pygame.sprite.Group,
        enemy_collision_sprites: pygame.sprite.Group,
        player_sprite: pygame.sprite.Group,
    ) -> None:
        super().__init__(*groups)
        self.image = pygame.Surface((64, 64))
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill(pygame.Color("black"))
        self.velocity = pygame.Vector2((6, 0))
        self.collision_sprites = collision_sprites
        self.player_sprite = player_sprite
        self.enemy_collision_sprites = enemy_collision_sprites

    def horizontal_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if self.rect is not None and sprite.rect is not None:
                if sprite.rect.colliderect(self.rect):
                    if self.velocity.x < 0:
                        self.rect.left = sprite.rect.right
                        self.velocity.x *= -1
                    elif self.velocity.x > 0:
                        self.velocity *= -1
                        self.rect.right = sprite.rect.left
        for sprite in self.enemy_collision_sprites.sprites():
            if self.rect is not None and sprite.rect is not None:
                if sprite.rect.colliderect(self.rect):
                    if self.velocity.x < 0:
                        self.rect.left = sprite.rect.right
                        self.velocity.x *= -1
                    elif self.velocity.x > 0:
                        self.velocity *= -1
                        self.rect.right = sprite.rect.left

    def vertical_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if self.rect is not None and sprite.rect is not None:
                if sprite.rect.colliderect(self.rect):
                    if self.velocity.y < 0:
                        self.rect.top = sprite.rect.bottom
                        self.velocity.y = 0
                    if self.velocity.y > 0:
                        self.rect.bottom = sprite.rect.top
                        self.velocity.y = 0

    def checkPlayer(self):
        for player in self.player_sprite:
            if self.rect.colliderect(player.rect):
                self.kill()

    def move(self) -> None:
        for player in self.player_sprite:
            if abs(player.rect.x - self.rect.x) < 300:
                if self.rect.x - 5 > player.rect.x:
                    self.velocity.x = -7
                if self.rect.x + 5 < player.rect.x:
                    self.velocity.x = 7
                if self.rect.x == player.rect.x:
                    self.velocity.x = 0

    def update(self) -> None:
        self.rect.x += self.velocity.x
        self.move()
        self.horizontal_collisions()
        self.checkPlayer()
