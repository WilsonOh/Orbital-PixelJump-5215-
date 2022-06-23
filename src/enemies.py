import pygame
from assets import get_sprite_image
from animations import load_animation, change_action

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
        self.speed = 5
        self.velocity = pygame.Vector2((self.speed, 0))
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
                        self.rect.right = sprite.rect.left
                        self.velocity *= -1
        for sprite in self.enemy_collision_sprites.sprites():
            if self.rect is not None and sprite.rect is not None:
                if sprite.rect.colliderect(self.rect):
                    if self.velocity.x < 0:
                        self.rect.left = sprite.rect.right
                        self.velocity.x *= -1
                    elif self.velocity.x > 0:
                        self.rect.right = sprite.rect.left
                        self.velocity *= -1

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
            if abs(player.rect.x - self.rect.x) < 200:
                if self.rect.x == player.rect.x:
                    self.velocity.x = 0
                elif self.rect.x + 5 > player.rect.x:
                    self.velocity.x = -1 * self.speed
                elif self.rect.x - 5 < player.rect.x:
                    self.velocity.x = self.speed

    def update(self) -> None:
        self.rect.x += self.velocity.x
        self.horizontal_collisions()
        self.move()
        self.checkPlayer()


class MushroomEnemy(Enemy):
    def __init__(
            self,
            pos: tuple[int, int],
            *groups: pygame.sprite.AbstractGroup,
            collision_sprites: pygame.sprite.Group,
            enemy_collision_sprites: pygame.sprite.Group,
            player_sprite: pygame.sprite.Group,
    ) -> None:
        super().__init__(pos,
                         *groups,
                         collision_sprites=collision_sprites,
                         enemy_collision_sprites=enemy_collision_sprites,
                         player_sprite=player_sprite)
        self.image = get_sprite_image("mushroom", [64, 64])
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 3
        self.velocity = pygame.Vector2((self.speed, 0))
        self.collision_sprites = collision_sprites
        self.player_sprite = player_sprite
        self.enemy_collision_sprites = enemy_collision_sprites

        # For animations
        self.animation_images = {}
        self.animation_database = {
            "walking": load_animation(
                "mushroom_walking", [7, 7, 7, 7, 7, 7, 7, 7, 7, 7], self.animation_images
            ),
            "idle": load_animation(
                "mushroom_idle", [10], self.animation_images
            ),
        }
        self.enemy_action = "idle"
        self.enemy_frame = 0
        self.enemy_flip = False

    def animation(self):
        if self.velocity.x > 0:
            self.enemy_action, self.enemy_frame = change_action(
                self.enemy_action, self.enemy_frame, "walking"
            )
            self.enemy_flip = False

        if self.velocity.x == 0:
            self.enemy_action, self.enemy_frame = change_action(
                self.enemy_action, self.enemy_frame, "idle"
            )

        if self.velocity.x < 0:
            self.enemy_action, self.enemy_frame = change_action(
                self.enemy_action, self.enemy_frame, "walking"
            )
            self.enemy_flip = True

    def animating_image(self):
        self.enemy_frame += 1
        if self.enemy_frame >= len(self.animation_database[self.enemy_action]):
            self.enemy_frame = 0
        enemy_img_id = self.animation_database[self.enemy_action][self.enemy_frame]
        enemy_image = self.animation_images[enemy_img_id]
        self.image = pygame.transform.flip(enemy_image, self.enemy_flip, False)

    def update(self) -> None:
        self.animation()
        self.animating_image()
        self.rect.x += self.velocity.x
        self.horizontal_collisions()
        self.move()
        self.checkPlayer()


class FroggyEnemy(Enemy):
    def __init__(
            self,
            pos: tuple[int, int],
            *groups: pygame.sprite.AbstractGroup,
            collision_sprites: pygame.sprite.Group,
            enemy_collision_sprites: pygame.sprite.Group,
            player_sprite: pygame.sprite.Group,
    ) -> None:
        super().__init__(pos,
                         *groups,
                         collision_sprites=collision_sprites,
                         enemy_collision_sprites=enemy_collision_sprites,
                         player_sprite=player_sprite)
        self.image = get_sprite_image("froggy", [64, 64])
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 6
        self.velocity = pygame.Vector2((self.speed, 0))
        self.collision_sprites = collision_sprites
        self.player_sprite = player_sprite
        self.enemy_collision_sprites = enemy_collision_sprites

        # For animations
        self.animation_images = {}
        self.animation_database = {
            "walking": load_animation(
                "froggy_walking", [7, 7, 7, 7, 7, 7, 7, 7, 7, 7], self.animation_images
            ),
            "idle": load_animation(
                "froggy_idle", [7, 7, 7, 7], self.animation_images
            ),
        }
        self.enemy_action = "idle"
        self.enemy_frame = 0
        self.enemy_flip = True

    def animation(self):
        if self.velocity.x > 0:
            self.enemy_action, self.enemy_frame = change_action(
                self.enemy_action, self.enemy_frame, "walking"
            )
            self.enemy_flip = True

        if self.velocity.x == 0:
            self.enemy_action, self.enemy_frame = change_action(
                self.enemy_action, self.enemy_frame, "idle"
            )

        if self.velocity.x < 0:
            self.enemy_action, self.enemy_frame = change_action(
                self.enemy_action, self.enemy_frame, "walking"
            )
            self.enemy_flip = False

    def animating_image(self):
        self.enemy_frame += 1
        if self.enemy_frame >= len(self.animation_database[self.enemy_action]):
            self.enemy_frame = 0
        enemy_img_id = self.animation_database[self.enemy_action][self.enemy_frame]
        enemy_image = self.animation_images[enemy_img_id]
        self.image = pygame.transform.flip(enemy_image, self.enemy_flip, False)

    def update(self) -> None:
        self.animation()
        self.animating_image()
        self.rect.x += self.velocity.x
        self.horizontal_collisions()
        self.move()
        self.checkPlayer()








