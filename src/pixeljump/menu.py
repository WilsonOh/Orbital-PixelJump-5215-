import sys

from pixeljump.assets import get_music, get_sprite_image
from pixeljump.settings import load_settings
import pygame

settings = load_settings()

WINDOW_WIDTH = int(settings["window"]["screen_width"])
WINDOW_HEIGHT = int(settings["window"]["screen_height"])


def pause_screen():
    pause_image = get_sprite_image("pause", (WINDOW_WIDTH, WINDOW_HEIGHT))
    window = pygame.display.get_surface()
    pause_out_sound = get_music("pause_out.wav")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_out_sound.play()
                    return
                if event.key == pygame.K_q:
                    sys.exit()
        window.fill(pygame.Color("white"))
        window.blit(pause_image, [0, 0])
        pygame.display.update()


def menu():
    menu_image = get_sprite_image("menu", (WINDOW_WIDTH, WINDOW_HEIGHT))
    window = pygame.display.get_surface()
    menu_sound = get_music("menu_sound.wav")
    menu_music = get_music("100_victories.wav")
    menu_music.set_volume(0.2)

    menu_music.play()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    pygame.mixer.Channel(1).play(menu_sound)
                    menu_music.fadeout(1000)
                    return
        window.blit(menu_image, [0, 0])
        pygame.display.update()


def win_screen():
    window = pygame.display.get_surface()
    font = pygame.font.SysFont("arial", int(window.get_height() * 0.05))
    title = font.render(
        "YOU WIN! Press Enter to continue or Q to exit the game",
        True,
        pygame.Color("black"),
    )
    win_center = window.get_rect().center
    title_center = title.get_rect().center
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    clock = pygame.time.Clock()
                    from pixeljump.levels.act2 import ActTwo

                    level = ActTwo()
                    while True:
                        level.run(clock)
                        clock.tick_busy_loop(60)
                        pygame.display.update()

        window.fill(pygame.Color("yellow"))
        window.blit(
            title, (win_center[0] - title_center[0], win_center[1] - title_center[1])
        )
        pygame.display.update()
