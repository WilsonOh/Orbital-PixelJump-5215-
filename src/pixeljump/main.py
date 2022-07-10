import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

pygame.init()
from pixeljump.levels.act1 import ActOne
from pixeljump.levels.act2 import ActTwo
from pixeljump.menu import show_menu
from pixeljump.settings import load_settings
from pixeljump.assets import get_sprite_image


settings = load_settings()


WIDTH = settings["window"]["screen_width"]
HEIGHT = settings["window"]["screen_height"]


def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PIXELJUMP")
    pygame.display.set_icon(get_sprite_image("KNIGHT", (32, 32)))
    act = show_menu()
    if act == 0 or act == 1:
        ActOne().run()
        ActTwo().run()
    if act == 2:
        ActTwo().run()


if __name__ == "__main__":
    main()
