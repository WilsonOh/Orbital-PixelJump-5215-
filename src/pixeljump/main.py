import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
from pixeljump.level import Level
from pixeljump.menu import menu
from pixeljump.settings import load_settings

import pygame


settings = load_settings()
WIDTH = settings["window"]["screen_width"]
HEIGHT = settings["window"]["screen_height"]
BG_COLOR = settings["colors"]["bg"]
FPS = settings["window"]["fps"]


def main():
    pygame.init()
    pygame.mixer.pre_init(44100, -16, 2, 512)
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PIXELJUMP")
    clock = pygame.time.Clock()
    menu()
    level = Level()

    while True:
        window.fill(BG_COLOR)
        level.run(clock)
        pygame.display.update()
        clock.tick_busy_loop(FPS)


if __name__ == "__main__":
    main()
