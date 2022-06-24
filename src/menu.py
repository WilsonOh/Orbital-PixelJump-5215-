import pygame
from assets import get_sprite_image, get_music
from settings import load_settings

settings = load_settings()

WINDOW_WIDTH = settings["window"]["screen_width"]
WINDOW_HEIGHT = settings["window"]["screen_height"]


def pause_screen():
    pause_image = get_sprite_image("pause", [WINDOW_WIDTH, WINDOW_HEIGHT])
    window = pygame.display.get_surface()
    pause_out_sound = get_music("pause_out.wav")
    font = pygame.font.SysFont("arial", int(window.get_height() * 0.05))
    text = font.render(
        "GAME PAUSED, PRESS ESCAPE TO RETURN or q to QUIT", True, pygame.Color("black")
    )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_out_sound.play()
                    return
                if event.key == pygame.K_q:
                    quit()
        window.fill(pygame.Color("white"))
        '''
        window.blit(
            text,
            (
                int(window.get_width() // 2 - text.get_width() // 2),
                int(window.get_height() // 2 - text.get_height() // 2),
            ),
        )
        '''
        window.blit(pause_image, [0, 0])
        pygame.display.update()


def menu():
    menu_image = get_sprite_image("menu", [WINDOW_WIDTH, WINDOW_HEIGHT])
    window = pygame.display.get_surface()
    font = pygame.font.SysFont("arial", int(window.get_height() * 0.05))
    title = font.render("PIXELJUMP", True, pygame.Color("black"))
    menu_sound = get_music("menu_sound.wav")

    option_strings = ["Press ENTER to start the game", "Press ESCAPE to quit the game"]
    options_texts = [
        font.render(option_string, True, pygame.Color("red"))
        for option_string in option_strings
    ]
    win_center = window.get_rect().center
    title_center = title.get_rect().center
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                if event.key == pygame.K_RETURN:
                    menu_sound.play()
                    return
        '''
        window.fill(pygame.Color("white"))
        window.blit(
            title, (win_center[0] - title_center[0], win_center[1] - title_center[1])
        )
        '''
        window.blit(menu_image, [0, 0])
        pygame.display.update()
