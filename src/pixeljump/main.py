import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame

pygame.init()

from pixeljump.settings import load_settings

settings = load_settings()

from pixeljump.levels.act1 import ActOne
from pixeljump.levels.act2 import ActTwo
from pixeljump.menu import show_menu


WIDTH = settings["window"]["screen_width"]
HEIGHT = settings["window"]["screen_height"]


def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PIXELJUMP")
    act = show_menu()
    if act == 0 or act == 1:
        ActOne().run()
        ActTwo().run()
    if act == 2:
        ActTwo().run()


if __name__ == "__main__":
    main()
