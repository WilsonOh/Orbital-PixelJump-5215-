import pygame


def pause_screen():
    window = pygame.display.get_surface()
    font = pygame.font.SysFont("arial", int(window.get_height() * 0.05))
    text = font.render(
        "GAME PAUSED, PRESS ESCAPE TO RETURN", True, pygame.Color("black")
    )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        window.fill(pygame.Color("white"))
        window.blit(
            text,
            (
                int(window.get_width() // 2 - text.get_width() // 2),
                int(window.get_height() // 2 - text.get_height() // 2),
            ),
        )
        pygame.display.update()


def menu():
    window = pygame.display.get_surface()
    font = pygame.font.SysFont("arial", int(window.get_height() * 0.05))
    title = font.render("PIXELJUMP", True, pygame.Color("black"))

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
                    return
        window.fill(pygame.Color("white"))
        window.blit(
            title, (win_center[0] - title_center[0], win_center[1] - title_center[1])
        )
        pygame.display.update()
