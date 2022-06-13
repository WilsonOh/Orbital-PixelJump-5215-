import pygame

from level import Level
from settings import load_settings

settings = load_settings()
WIDTH = settings["window"]["screen_width"]
HEIGHT = settings["window"]["screen_height"]
BG_COLOR = settings["colors"]["bg"]
FPS = settings["window"]["fps"]

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Platformer")
clock = pygame.time.Clock()
level = Level()

while True:
    window.fill(BG_COLOR)
    level.run(clock)
    pygame.display.update()
    clock.tick_busy_loop(FPS)
