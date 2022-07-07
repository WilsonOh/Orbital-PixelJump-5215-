import pygame
from pixeljump.settings import load_settings
from pixeljump.animations import load_particles
from pixeljump.assets import get_sprite_image

settings = load_settings()

GRAVITY = settings["player"]["gravity"]
GRAVITY = 0


class Particles(pygame.sprite.Sprite):
    def __init__(
        self,
        pos: tuple[int, int],
        velocity: tuple[int, int],
        *groups: pygame.sprite.AbstractGroup
    ):
        super().__init__(*groups)
        self.pos = pos
        self.velocity = pygame.Vector2((velocity[0], velocity[1]))
        self.gravity = GRAVITY
        self.image = get_sprite_image("particle", (0, 0))
        self.rect = self.image.get_rect(topleft=pos)

        # For animations
        self.animation_images: dict[str, pygame.Surface] = {}
        self.animation_database = {
            "particle": load_particles(
                "particle", [7, 7, 7, 7, 7, 7], self.animation_images
            )
        }
        self.particle_action = "particle"
        self.particle_frame = 0

    def animating_image(self):
        self.particle_frame += 1
        if self.particle_frame >= len(self.animation_database[self.particle_action]):
            self.kill()
            return
        particle_img_id = self.animation_database[self.particle_action][
            self.particle_frame
        ]
        particle_image = self.animation_images[particle_img_id]
        self.image = particle_image

    def update(self):
        self.animating_image()
        self.rect.x += int(self.velocity.x)
        self.velocity.y += GRAVITY
        self.rect.y += self.velocity.y
