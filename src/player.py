import pygame
from settings import load_settings
from assets import get_sprite_image

settings = load_settings()

TILE_SIZE = settings["window"]["tile_size"]
PLAYER_COLOR = settings["colors"]["player"]
FPS = settings["window"]["fps"]
PLAYER_HORIZONTAL_VEL = settings["player"]["horizontal_velocity"]
PLAYER_VERTICAL_VEL = settings["player"]["vertical_velocity"]
GRAVITY = settings["player"]["gravity"]


class Player(pygame.sprite.Sprite):
    def __init__(
        self,
        position: tuple[int, int],
        *groups: pygame.sprite.Group,
        collision_sprites: pygame.sprite.Group
    ):
        super().__init__(*groups)
        self.image = get_sprite_image("KNIGHT", (TILE_SIZE, TILE_SIZE), convert=False)
        self.rect = self.image.get_rect(topleft=position)
        self.velocity = pygame.Vector2()
        self.collision_sprites = collision_sprites
        self.death_count = 0
        self.can_jump = True
        self.can_double_jump = True

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # and 0 < self.rect.x:
            self.velocity.x = -PLAYER_HORIZONTAL_VEL
        elif (
            keys[pygame.K_d]
            # and self.rect.x < pygame.display.get_window_size()[0] - self.rect.width
        ):
            self.velocity.x = PLAYER_HORIZONTAL_VEL
        else:
            self.velocity.x = 0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.can_jump:
                        self.velocity.y = -PLAYER_VERTICAL_VEL
                        self.can_jump = False
                    elif self.can_double_jump:
                        self.velocity.y = -PLAYER_VERTICAL_VEL
                        self.can_double_jump = False
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

    def horizontal_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if self.rect is not None and sprite.rect is not None:
                if sprite.rect.colliderect(self.rect):
                    if self.velocity.x < 0:
                        self.rect.left = sprite.rect.right
                    if self.velocity.x > 0:
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
                        self.can_jump = True
                        self.can_double_jump = True

    def apply_gravity(self):
        self.velocity.y += GRAVITY
        self.rect.y += self.velocity.y

    def check_alive(self):
        window = pygame.display.get_surface()
        font = pygame.font.SysFont("comicsans", 50, bold=True)
        text = font.render("YOU DIED", True, pygame.Color("red"))
        if self.rect.y > pygame.display.get_window_size()[1] * 2:
            window.blit(
                text,
                (
                    window.get_width() // 2 - text.get_width() // 2,
                    window.get_height() // 2 - text.get_height() // 2,
                ),
            )
            self.death_count += 1
            if self.death_count > 1.5 * FPS:
                pygame.quit()
                quit()

    def update(self):
        self.input()
        self.rect.x += self.velocity.x
        self.horizontal_collisions()
        self.apply_gravity()
        self.vertical_collisions()
        self.check_alive()
