import pygame, random
from settings import load_settings
from assets import get_sprite_image
from animations import load_animation, change_action

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

        # For animations
        self.animation_images = {}
        self.animation_database = {'idle': load_animation('idle', [7, 7, 40], self.animation_images),
                                   'running': load_animation('running', [7, 7, 7, 7, 7, 7, 7, 7],
                                                             self.animation_images)}
        self.player_action = 'idle'
        self.player_frame = 0
        self.player_flip = False

        # For audio
        self.jump_sound = pygame.mixer.Sound('../assets/music/jump.wav')
        self.jump_sound.set_volume(0.5)
        self.step_sound = [pygame.mixer.Sound('../assets/music/step0.wav'),
                           pygame.mixer.Sound('../assets/music/step1.wav')]
        self.step_sound_timer = 0
        self.step_sound[0].set_volume(0.5)
        self.step_sound[1].set_volume(0.5)

    def input(self):
        if self.step_sound_timer > 0:
            self.step_sound_timer -= 1

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
                        self.jump_sound.play()
                    elif self.can_double_jump:
                        self.velocity.y = -PLAYER_VERTICAL_VEL
                        self.can_double_jump = False
                        self.jump_sound.play()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

    def animation(self):
        if self.velocity.x > 0:
            self.player_action, self.player_frame = change_action(self.player_action, self.player_frame, 'running')
            self.player_flip = False

        if self.velocity.x == 0:
            self.player_action, self.player_frame = change_action(self.player_action, self.player_frame, 'idle')

        if self.velocity.x < 0:
            self.player_action, self.player_frame = change_action(self.player_action, self.player_frame, 'running')
            self.player_flip = True

    def animating_image(self):
        self.player_frame += 1
        if self.player_frame >= len(self.animation_database[self.player_action]):
            self.player_frame = 0
        player_img_id = self.animation_database[self.player_action][self.player_frame]
        player_image = self.animation_images[player_img_id]
        self.image = pygame.transform.flip(player_image, self.player_flip, False)

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
                        if self.velocity.x != 0:
                            if self.step_sound_timer == 0:
                                self.step_sound_timer = 30
                                random.choice(self.step_sound).play()

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
        self.animation()
        self.animating_image()
        self.rect.x += self.velocity.x
        self.horizontal_collisions()
        self.apply_gravity()
        self.vertical_collisions()
        self.check_alive()


